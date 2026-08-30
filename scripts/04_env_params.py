import json
from pathlib import Path
import _bootstrap
from fortyguard import FortyGuardClient
from samples import SAN_ANTONIO_POINT

def fetch_san_antonio_env_params():
    client = FortyGuardClient()
    print("[San Antonio] Submitting Environmental Parameters request...")
    response = client.environmental_parameters(
        latitude=SAN_ANTONIO_POINT["latitude"],
        longitude=SAN_ANTONIO_POINT["longitude"],
        temperature=37.5,
        start_date="2024-07-15",
        start_time="12:00",
        end_time="18:00",
        filter_type=2,
        analysis=["heat_index_celsius", "apparent_temperature_celsius", "relative_humidity_percent"],
        wait=True,
        verbose=True
    )
    cache_path = Path("thermomind/cache/san_antonio_env_params.json")
    cache_path.parent.mkdir(parents=True, exist_ok=True)
    cache_path.write_text(json.dumps(response, indent=2))
    print(f"Saved San Antonio Env Params response to {cache_path}")

if __name__ == "__main__":
    fetch_san_antonio_env_params()