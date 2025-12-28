# backend/tests/test_main_routes.py
import pytest
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

# ---------------------------
# Test /api/health endpoint
# ---------------------------
def test_health():
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

# ---------------------------
# Test /api/distribution endpoint
# ---------------------------
def test_distribution():
    response = client.get("/api/distribution?hours=24")
    assert response.status_code == 200
    data = response.json()
    assert "positive" in data
    assert "negative" in data
    assert "neutral" in data

# ---------------------------
# Test /api/aggregate endpoint
# ---------------------------
def test_aggregate():
    response = client.get("/api/aggregate?period=hour")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert "timestamp" in data[0]
    assert "positive" in data[0]
    assert "negative" in data[0]
    assert "neutral" in data[0]

# ---------------------------
# Test /api/posts endpoint
# ---------------------------
def test_posts():
    response = client.get("/api/posts?limit=10&offset=0")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert "text" in data[0]
    assert "sentiment" in data[0]
    assert "timestamp" in data[0]

# ---------------------------
# Test WebSocket endpoint
# ---------------------------
def test_websocket():
    with client.websocket_connect("/ws") as ws:
        data = ws.receive_json()
        assert data["type"] == "distribution_update"
        assert "positive" in data["data"]
        assert "negative" in data["data"]
        assert "neutral" in data["data"]
