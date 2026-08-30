import os
import re
import unicodedata
from pathlib import Path

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parent / ".env")


class OpenSourceThermoMindAgent:
    DEFAULT_MODELS = [
        "llama-3.3-70b-versatile",
        "llama-3.1-8b-instant",
        "openai/gpt-oss-20b",
        "meta-llama/llama-4-scout-17b-16e-instruct",
    ]

    def __init__(self):
        api_key = os.getenv("OPEN_SOURCE_API_KEY") or os.getenv("FORTYGUARD_API_KEY")
        self.client = None
        configured_model = os.getenv("OPEN_SOURCE_MODEL")
        self.model_name = configured_model or self.DEFAULT_MODELS[0]

        if api_key:
            self.client = OpenAI(
                base_url=os.getenv("OPEN_SOURCE_BASE_URL", "https://api.groq.com/openai/v1"),
                api_key=api_key,
            )

    def _format_response(self, answer: str) -> str:
        cleaned = (answer or "").strip()
        cleaned = unicodedata.normalize("NFKC", cleaned)
        cleaned = cleaned.replace("\r", "")
        
        if not cleaned:
            return "How may I assist you with urban heat planning today?"
        
        # AGGRESSIVE FILTER: Strip out any PDF creation advice or links the AI tries to write
        forbidden_phrases = [
            "PDF Creation Instructions", "word processor", "Microsoft Word", 
            "Google Docs", "Smallpdf", "ILovePDF", "online converter", 
            "Save As", "Export or Save"
        ]
        for phrase in forbidden_phrases:
            if phrase in cleaned:
                # Cut off the response before the unwanted instructions
                cleaned = cleaned.split(phrase)[0].strip()

        cleaned = re.sub(r"\s+-\s+", "\n\n- ", cleaned)
        cleaned = re.sub(r"\s+\*\s+", "\n\n* ", cleaned)
        return cleaned

    def _call_model(self, messages: list[dict], temperature: float = 0.2):
        if self.client is None:
            raise RuntimeError("No AI client configured.")

        attempts = []
        configured = os.getenv("OPEN_SOURCE_MODEL")
        if configured:
            attempts.append(configured)
        attempts.extend(model for model in self.DEFAULT_MODELS if model not in attempts)

        last_error = None
        for model_name in attempts:
            try:
                response = self.client.chat.completions.create(
                    model=model_name,
                    messages=messages,
                    temperature=temperature,
                )
                content = getattr(response.choices[0].message, "content", None)
                if content:
                    return content
            except Exception as exc:
                last_error = exc

        if last_error is not None:
            raise last_error
        raise RuntimeError("No model available for the ThermoMind agent.")

    def answer_question(self, question: str, data_context: str, history: list[dict] | None = None) -> str:
        lower_q = question.lower().strip()

        # Handle direct casual greetings natively
        if lower_q in ["hi", "hello", "hey", "greetings", "hi!"]:
            return "Hello! How may I assist you with urban heat planning or cooling strategies today?"

        if self.client is None:
            return "Hello! How may I assist you with urban heat intelligence today?"

        messages = [
            {
                "role": "system",
                "content": (
                    "You are ThermoMind, a smart and helpful urban heat intelligence AI assistant. "
                    "CRITICAL BEHAVIOR RULES:\n"
                    "1. MATCH USER INTENT STRICTLY:\n"
                    "   - If the user says hello or 'hi', reply warmly: 'Hello! How may I assist you with urban heat planning today?' DO NOT dump data.\n"
                    "   - If the user asks where to intervene first, identify ONLY the single highest-risk tile/area from the context.\n"
                    "   - If the user asks about cooling a house, building, park, or bus stop, give targeted advice specific to that exact structure or location without listing unrelated database tiles.\n"
                    "   - If the user asks to compare areas, provide a concise comparative breakdown.\n"
                    "   - If the user asks what to wear, bring, or how to protect themselves when going outside, give practical personal heat-safety and protection advice.\n"
                    "2. FORMATTING: Use clean paragraphs and bullet points with proper spacing (`\\n\\n`). Never lump multiple bullet items into a single line.\n"
                    "3. NO MANUAL PDF INSTRUCTIONS: Never include text, instructions, or steps telling the user how to create a PDF report or copy text manually, as the application generates PDF reports automatically via export buttons."
                ),
            },
            {"role": "system", "content": f"Available FortyGuard context & telemetry:\n{data_context}"},
        ]
        if history:
            messages.extend(history[-8:])
        messages.append({"role": "user", "content": question})

        try:
            response_text = self._call_model(messages, temperature=0.2)
        except Exception as exc:
            print(f"⚠️ LIVE AGENT ERROR: {exc}")
            return "Hello! How may I assist you with your heat resilience planning today?"
        
        return self._format_response(response_text)