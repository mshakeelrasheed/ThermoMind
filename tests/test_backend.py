from fastapi.testclient import TestClient

from backend import create_app


def test_backend_health_and_dashboard():
    client = TestClient(create_app())

    health = client.get("/health")
    assert health.status_code == 200
    assert health.json()["status"] == "ok"

    dashboard = client.get("/api/dashboard")
    assert dashboard.status_code == 200
    assert "datasets" in dashboard.json()
    assert "ranked_zones" in dashboard.json()
