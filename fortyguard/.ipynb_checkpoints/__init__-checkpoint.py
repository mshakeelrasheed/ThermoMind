import os
import time
from typing import Any

import requests
from dotenv import load_dotenv


class FortyGuardClient:
    """Small HTTP client compatible with the methods used by ThermoMind."""

    def __init__(self, api_key: str | None = None, base_url: str | None = None):
        load_dotenv()
        self.api_key = api_key or os.getenv("FORTYGUARD_API_KEY")
        self.base_url = (base_url or os.getenv("FORTYGUARD_BASE_URL", "")).rstrip("/")
        if not self.api_key or self.api_key == "your_fortyguard_api_key_here":
            raise ValueError("Set a valid FORTYGUARD_API_KEY in .env")
        if not self.base_url:
            raise ValueError("Set FORTYGUARD_BASE_URL in .env")

    def _headers(self) -> dict[str, str]:
        return {
            "Authorization": f"Bearer {self.api_key}",
            "X-API-Key": self.api_key,
            "api-key": self.api_key,
            "Accept": "application/json",
        }

    def _poll_result(self, response: dict[str, Any]) -> dict[str, Any]:
        activity_id = response.get("data", {}).get("activity_id")
        if not activity_id:
            return response

        timeout = float(os.getenv("FORTYGUARD_POLL_TIMEOUT", "120"))
        interval = float(os.getenv("FORTYGUARD_POLL_INTERVAL", "2"))
        deadline = time.monotonic() + timeout
        while time.monotonic() < deadline:
            status_response = requests.get(
                f"{self.base_url}/v1/status/{activity_id}",
                headers=self._headers(),
                timeout=30,
            )
            if not status_response.ok:
                detail = status_response.text.strip()
                raise requests.HTTPError(
                    f"{status_response.status_code} {status_response.reason} for {status_response.url}"
                    + (f": {detail}" if detail else ""),
                    response=status_response,
                )

            status_payload = status_response.json()
            status_data = status_payload.get("data", status_payload)
            status = str(status_data.get("status", status_payload.get("status", ""))).lower()
            result = self._find_result(status_payload)
            if result is not None:
                return result
            if status in {"failed", "error", "cancelled", "canceled"}:
                raise RuntimeError(f"FortyGuard activity {activity_id} failed: {status_payload}")
            time.sleep(interval)

        raise TimeoutError(
            f"FortyGuard activity {activity_id} did not complete within {timeout:g} seconds"
        )

    def _find_result(self, value: Any) -> dict[str, Any] | None:
        if isinstance(value, dict):
            if value.get("map_data") or value.get("features") or value.get("stats_data"):
                return value
            for nested in value.values():
                result = self._find_result(nested)
                if result is not None:
                    return result
        elif isinstance(value, list):
            for nested in value:
                result = self._find_result(nested)
                if result is not None:
                    return result
        return None

    def _post(self, path: str, payload: dict[str, Any]) -> dict[str, Any]:
        if "date_time" not in payload and payload.get("start_date") and payload.get("start_time"):
            payload = {
                **payload,
                "date_time": {
                    "start_date": payload["start_date"],
                    "start_time": payload["start_time"],
                    "end_date": payload.get("end_date"),
                    "end_time": payload.get("end_time"),
                    "filter_type": payload.get("filter_type"),
                },
            }
        response = requests.post(
            f"{self.base_url}/{path.lstrip('/')}",
            json=payload,
            headers=self._headers(),
            timeout=120,
        )
        if not response.ok:
            detail = response.text.strip()
            raise requests.HTTPError(
                f"{response.status_code} {response.reason} for {response.url}"
                + (f": {detail}" if detail else ""),
                response=response,
            )
        return self._poll_result(response.json())

    def create_heatmap(self, **payload: Any) -> dict[str, Any]:
        return self._post("v1/heatmap", payload)

    def environmental_parameters(self, **payload: Any) -> dict[str, Any]:
        return self._post("v1/env_params", payload)

    def satellite_segmentation(self, **payload: Any) -> dict[str, Any]:
        if "sat" not in payload and payload.get("latitude") is not None and payload.get("longitude") is not None:
            payload = {
                **payload,
                "sat": {
                    "latitude": payload["latitude"],
                    "longitude": payload["longitude"],
                },
                "date_time": {
                    "start_date": payload.get("start_date"),
                    "filter_type": payload.get("filter_type"),
                },
            }
        return self._post("v1/satellite", payload)
