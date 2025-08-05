import pytest
from models.user_models import User
from services import user_service
from schemas.user_schemas import UserResponse, UsersListResponse, UserOut, UserCreate
from fastapi import HTTPException


def test_get_user_by_id_success(mocker, fake_db_session):
    fake_user = User(id=1, email="test@example.com", first_name="Test", last_name="User", avatar="https://example.com/avatar.jpg")
    mocker.patch("repositories.user_repository.get_user_by_id", return_value=fake_user)

    result = user_service.get_user_by_id(1, fake_db_session)
    assert isinstance(result, UserResponse)
    assert result.data.id == 1


def test_get_user_by_id_not_found(mocker, fake_db_session):
    mocker.patch("repositories.user_repository.get_user_by_id", return_value=None)

    with pytest.raises(HTTPException) as exc:
        user_service.get_user_by_id(999, fake_db_session)

    assert exc.value.status_code == 404
    assert exc.value.detail == "User not found"


def test_get_users_paginated(mocker, fake_db_session):
    # Мокаем количество пользователей
    mocker.patch("repositories.user_repository.get_total_users_count", return_value=6)

    # Мокаем список пользователей
    fake_users = [
        User(id=i, email=f"user{i}@test.com", first_name="User", last_name=str(i), avatar="https://example.com/avatar.jpg")
        for i in range(6)
    ]
    mocker.patch("repositories.user_repository.get_users_paginated", return_value=fake_users)

    result = user_service.get_users_paginated(page=1, per_page=6, db=fake_db_session)

    assert isinstance(result, UsersListResponse)
    assert result.total == 6
    assert result.total_pages == 1
    assert len(result.data) == 6


def test_create_user_success(mocker, fake_db_session):
    user_data = UserCreate(
        email="test@example.com",
        first_name="Test",
        last_name="User",
        avatar=None
    )

    fake_user = User(id=1, email=user_data.email, first_name="Test", last_name="User", avatar="https://example.com/avatar.jpg")
    mocker.patch("repositories.user_repository.create_user", return_value=fake_user)

    result = user_service.create_user(user_data, fake_db_session)

    assert isinstance(result, UserOut)
    assert result.id == 1
    assert result.email == user_data.email


def test_delete_user_success(mocker, fake_db_session):
    mocker.patch("repositories.user_repository.soft_delete_user", return_value=True)

    result = user_service.delete_user(1, fake_db_session)

    assert result == {"message": "User 1 deleted"}


def test_delete_user_not_found(mocker, fake_db_session):
    mocker.patch("repositories.user_repository.soft_delete_user", return_value=False)

    with pytest.raises(HTTPException) as exc:
        user_service.delete_user(999, fake_db_session)

    assert exc.value.status_code == 404
    assert exc.value.detail == "User not found"
