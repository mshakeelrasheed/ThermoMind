import json
from pathlib import Path
import _bootstrap
from fortyguard import FortyGuardClient
from samples import SAN_ANTONIO_POINT

def fetch_san_antonio_satellite():
    client = FortyGuardClient()
    print("[San Antonio] Submitting Satellite Segmentation request...")
    response = client.satellite_segmentation(
        latitude=SAN_ANTONIO_POINT["latitude"],
        longitude=SAN_ANTONIO_POINT["longitude"],
        start_date="2024-07-15",
        filter_type=3,
        granularity=80,
        wait=True,
        verbose=True
    )
    cache_path = Path("thermomind/cache/san_antonio_satellite.json")
    cache_path.parent.mkdir(parents=True, exist_ok=True)
    cache_path.write_text(json.dumps(response, indent=2))
    print(f"Saved San Antonio Satellite segmentation to {cache_path}")

if __name__ == "__main__":
    fetch_san_antonio_satellite()