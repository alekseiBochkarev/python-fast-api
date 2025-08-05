from models.user_models import User
from repositories import user_repository
from schemas.user_schemas import UserCreate


def test_get_user_by_id_found(fake_db_session):
    fake_user = User(id=1, email="test@example.com", first_name="Test", last_name="User", avatar="url")
    fake_db_session.query().filter().first.return_value = fake_user

    result = user_repository.get_user_by_id(1, fake_db_session)
    assert result == fake_user


def test_get_user_by_id_not_found(fake_db_session):
    fake_db_session.query().filter().first.return_value = None

    result = user_repository.get_user_by_id(999, fake_db_session)
    assert result is None


def test_get_users_paginated(fake_db_session):
    fake_users = [User(id=i, email=f"user{i}@test.com", first_name="User", last_name=str(i), avatar="url") for i in
                  range(6)]
    fake_db_session.query().filter().offset().limit().all.return_value = fake_users

    result = user_repository.get_users_paginated(page=1, per_page=6, db=fake_db_session)
    assert len(result) == 6


def test_get_total_users_count(fake_db_session):
    fake_db_session.query().filter().count.return_value = 42

    result = user_repository.get_total_users_count(fake_db_session)
    assert result == 42


def test_create_user(fake_db_session):
    user_data = UserCreate(
        email="test@example.com",
        first_name="Test",
        last_name="User",
        avatar=None
    )

    # Мокаем поведение БД
    fake_db_session.add.return_value = None
    fake_db_session.commit.return_value = None
    fake_db_session.refresh.side_effect = lambda user: setattr(user, "id", 1)

    result = user_repository.create_user(user_data, fake_db_session)

    assert isinstance(result, User)
    assert result.id == 1
    assert result.email == user_data.email


def test_soft_delete_user_success(fake_db_session):
    user = User(id=1, is_deleted=False)
    fake_db_session.query().filter().first.return_value = user

    result = user_repository.soft_delete_user(1, fake_db_session)

    assert result is True
    assert user.is_deleted is True
    fake_db_session.commit.assert_called_once()


def test_soft_delete_user_not_found(fake_db_session):
    fake_db_session.query().filter().first.return_value = None

    result = user_repository.soft_delete_user(999, fake_db_session)

    assert result is False
