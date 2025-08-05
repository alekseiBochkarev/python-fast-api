import requests

BASE_URL = "http://localhost:8000"
def test_get_user_by_id_success(client):
    response = client.get("/api/users/2")
    assert response.status_code == 200
    data = response.json()
    assert data["data"]["id"] == 2
    assert "email" in data["data"]


def test_get_user_not_found(client):
    response = client.get("/api/users/9999")
    assert response.status_code == 404
    assert response.json()["detail"] == "User not found"
