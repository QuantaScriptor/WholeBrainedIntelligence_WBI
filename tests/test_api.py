
import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()

def test_analyze():
    test_data = {
        "text": "Test input",
        "features": [0.1, 0.2, 0.3]
    }
    response = client.post("/analyze", json=test_data)
    assert response.status_code == 200
    assert "complexity_score" in response.json()
