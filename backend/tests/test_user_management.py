from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_create_user():
    response = client.post("/users/", json={
        "username": "testuser",
        "email": "testuser@example.com",
        "password": "securepassword"
    })
    assert response.status_code == 200
    assert response.json()["username"] == "testuser"

def test_get_user():
    user_id = 1  # Replace with actual user ID from test data
    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200
    assert response.json()["id"] == user_id
