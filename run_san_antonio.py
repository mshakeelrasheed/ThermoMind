# thermomind/run_san_antonio.py

import json
from pathlib import Path
from risk_engine import ThermoMindRiskEngine
from agent import OpenSourceThermoMindAgent

def run_pipeline():
    print("🚀 Running ThermoMind Pipeline for San Antonio, TX...")
    
    cache_dir = Path("thermomind/cache")
    
    # Load cached San Antonio endpoint responses
    try:
        tcm_data = json.loads((cache_dir / "san_antonio_tcm.json").read_text())
        exceed_data = json.loads((cache_dir / "san_antonio_exceedance.json").read_text())
        persist_data = json.loads((cache_dir / "san_antonio_persistence.json").read_text())
    except FileNotFoundError:
        print("❌ Cache files missing! Run your endpoint scripts in thermomind/scripts/ first.")
        return

    # Rank zones using Risk Engine
    engine = ThermoMindRiskEngine()
    ranked_zones = engine.rank_zones(tcm_data, exceed_data, persist_data)

    if not ranked_zones:
        activity_id = tcm_data.get("data", {}).get("activity_id", "unknown")
        print(f"Heatmap activity submitted ({activity_id}), but no result features are available yet.")
        return

    top_zone = ranked_zones[0]
    print(f"\n🔥 Top Priority San Antonio Hotspot:")
    print(f"   Tile ID: {top_zone['tile_id']}")
    print(f"   Temperature: {top_zone['temperature']}°C")
    print(f"   Risk Score: {top_zone['risk_score']} ({top_zone['priority_tier']})")

    # Generate Open-Source AI Recommendation
    print("\n🤖 Generating Open-Source AI Agent Interventions...")
    try:
        agent = OpenSourceThermoMindAgent()
        advice = agent.generate_intervention_advice(top_zone)
        print("\n" + "="*50)
        print(advice)
        print("="*50)
    except Exception as e:
        print(f"AI Agent call skipped (check API configuration): {e}")

if __name__ == "__main__":
    run_pipeline()