import json
from pathlib import Path
import _bootstrap
from fortyguard import FortyGuardClient
from samples import SAN_ANTONIO_POLYGON

def fetch_san_antonio_exceedance():
    client = FortyGuardClient()
    print("[San Antonio] Submitting Exceedance analysis (Threshold: 35°C)...")
    response = client.create_heatmap(
        polygon_aoi=SAN_ANTONIO_POLYGON,
        start_date="2024-07-15",
        start_time="12:00",
        end_time="19:00",
        filter_type=2,
        granularity=100,
        analytic_type="exceedance",
        threshold=35.0,
        direction="above",
        wait=True,
        verbose=True
    )
    cache_path = Path("thermomind/cache/san_antonio_exceedance.json")
    cache_path.parent.mkdir(parents=True, exist_ok=True)
    cache_path.write_text(json.dumps(response, indent=2))
    print(f"Saved San Antonio Exceedance response to {cache_path}")

if __name__ == "__main__":
    fetch_san_antonio_exceedance()