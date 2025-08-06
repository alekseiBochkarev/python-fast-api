import pytest
import requests
from http import HTTPStatus
from models.user_models import User
from schemas.user_schemas import UserOut


@pytest.fixture()
def users(app_url):
    response = requests.get(f"{app_url}/api/users/")
    assert response.status_code == HTTPStatus.OK
    return response.json()


def test_users(app_url):
    response = requests.get(f"{app_url}/api/users/")
    assert response.status_code == HTTPStatus.OK

    users = response.json()
    for user in users["data"]:
        UserOut.model_validate(user)


def test_users_no_duplicates(users):
    users_ids = [user["id"] for user in users["data"]]
    assert len(users_ids) == len(set(users_ids))
    

def test_get_user_by_id_success(db_session, app_url):
    # 1. Получаем юзера из базы
    user = db_session.query(User).first()
    assert user is not None, "В базе нет ни одного пользователя"

    # 2. Делаем GET-запрос по ID
    response = requests.get(f"{app_url}/api/users/{user.id}")
    assert response.status_code == HTTPStatus.OK

    data = response.json()["data"]

    # 3. Сравниваем поля
    assert data["id"] == user.id
    assert data["email"] == user.email
    assert data["first_name"] == user.first_name
    assert data["last_name"] == user.last_name
    assert data["avatar"] == user.avatar


def test_get_user_not_found(db_session, app_url):
    max_id = db_session.query(User.id).order_by(User.id.desc()).first()
    # 2. Выбираем ID, которого точно нет
    non_existing_id = (max_id[0] if max_id else 0) + 1
    # 3. Делаем запрос
    response = requests.get(f"{app_url}/api/users/{non_existing_id}")
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json()["detail"] == "User not found"


@pytest.mark.parametrize("user_id", [-2, 0, "owl"])
def test_user_invalid_values(app_url, user_id):
    response = requests.get(f"{app_url}/api/users/{user_id}")
    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY
