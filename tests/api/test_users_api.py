import requests
from models.user_models import User

BASE_URL = "http://localhost:8000"


def test_get_user_by_id_success(db_session, client):
    user = db_session.query(User).first()
    assert user is not None, "В базе нет ни одного пользователя"

    # 2. Делаем GET-запрос по ID
    response = requests.get(f"{BASE_URL}/api/users/{user.id}")
    assert response.status_code == 200

    data = response.json()["data"]

    # 3. Сравниваем поля
    assert data["id"] == user.id
    assert data["email"] == user.email
    assert data["first_name"] == user.first_name
    assert data["last_name"] == user.last_name
    assert data["avatar"] == user.avatar


def test_get_user_not_found(client):
    response = requests.get(f"{BASE_URL}/api/users/9999")
    assert response.status_code == 404
    assert response.json()["detail"] == "User not found"
