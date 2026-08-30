from agent import OpenSourceThermoMindAgent


def test_agent_without_api_key_uses_fallback(monkeypatch):
    monkeypatch.delenv("OPEN_SOURCE_API_KEY", raising=False)
    monkeypatch.delenv("FORTYGUARD_API_KEY", raising=False)
    monkeypatch.setenv("OPEN_SOURCE_BASE_URL", "https://example.invalid")

    agent = OpenSourceThermoMindAgent()

    assert agent.client is None
    answer = agent.answer_question("Which blocks should get cool roofs first?", "zone summary")
    assert isinstance(answer, str)
    assert len(answer) > 80
    assert "- " in answer or "•" in answer
    assert len(answer.split()) < 300


def test_agent_uses_supported_default_groq_model(monkeypatch):
    monkeypatch.delenv("OPEN_SOURCE_MODEL", raising=False)
    agent = OpenSourceThermoMindAgent()
    assert agent.model_name in {"openai/gpt-oss-20b", "openai/gpt-oss-120b", "qwen/qwen3.8-27b"}
