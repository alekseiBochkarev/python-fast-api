import requests
from models.user_models import User

BASE_URL = "http://localhost:8000"


def test_get_user_by_id_success(db_session):
    # 1. Получаем юзера из базы
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


def test_get_user_not_found(db_session):
    max_id = db_session.query(User.id).order_by(User.id.desc()).first()
    # 2. Выбираем ID, которого точно нет
    non_existing_id = (max_id[0] if max_id else 0) + 1000

    # 3. Делаем запрос
    response = requests.get(f"{BASE_URL}/api/users/{non_existing_id}")
    assert response.status_code == 404
    assert response.json()["detail"] == "User not found"
