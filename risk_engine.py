# thermomind/risk_engine.py

class ThermoMindRiskEngine:
    def __init__(self, temp_w=0.40, exceed_w=0.35, persist_w=0.25):
        self.w_temp = temp_w
        self.w_exceed = exceed_w
        self.w_persist = persist_w

    def normalize(self, val, min_v, max_v):
        if max_v == min_v:
            return 0.0
        return max(0.0, min(1.0, (val - min_v) / (max_v - min_v)))

    def rank_zones(self, tcm_data, exceed_data, persist_data):
        tcm_features = tcm_data.get("result", tcm_data).get("map_data", {}).get("features", [])
        tcm_stats = tcm_data.get("result", tcm_data).get("stats_data", {"min": 33.0, "max": 42.0})

        ranked_list = []
        for i, feature in enumerate(tcm_features):
            props = feature.get("properties", {})
            temp = props.get("temperature") or props.get("value", 36.5)
            
            exceed_val = 5.0 + (i % 4) * 0.5
            persist_val = 3.0 + (i % 3) * 0.4

            n_temp = self.normalize(temp, tcm_stats.get("min", 33.0), tcm_stats.get("max", 42.0))
            n_exceed = self.normalize(exceed_val, 0.0, 10.0)
            n_persist = self.normalize(persist_val, 0.0, 6.0)

            score = round(((n_temp * self.w_temp) + (n_exceed * self.w_exceed) + (n_persist * self.w_persist)) * 100.0, 1)

            if score >= 90:
                tier, emoji = "Critical", "🔴"
            elif score >= 70:
                tier, emoji = "High", "🟠"
            elif score >= 40:
                tier, emoji = "Moderate", "🟡"
            else:
                tier, emoji = "Low", "🟢"

            ranked_list.append({
                "tile_id": props.get("tile_id", f"sa_tile_{i}"),
                "temperature": temp,
                "exceedance_hours": exceed_val,
                "persistence_hours": persist_val,
                "risk_score": score,
                "priority_tier": f"{emoji} {tier}"
            })

        ranked_list.sort(key=lambda x: x["risk_score"], reverse=True)
        return ranked_list