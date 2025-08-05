import pytest
from sqlalchemy.orm import Session
from fastapi.testclient import TestClient
from main import app
from models.db import SessionLocal


# Фикстура для тестового клиента FastAPI
@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def db_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture
def fake_db_session(mocker):
    return mocker.Mock(spec=Session)
