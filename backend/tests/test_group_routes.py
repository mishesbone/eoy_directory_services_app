from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_create_group():
    response = client.post("/groups/", json={
        "name": "Admins",
        "description": "Administrative group"
    })
    assert response.status_code == 200
    assert response.json()["name"] == "Admins"

def test_get_group():
    group_id = 1  # Replace with actual group ID from test data
    response = client.get(f"/groups/{group_id}")
    assert response.status_code == 200
    assert response.json()["id"] == group_id
