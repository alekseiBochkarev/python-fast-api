import sys
import os
import pytest
from sqlalchemy.orm import Session
from fastapi.testclient import TestClient
from main import app

# Добавляем корень проекта в PYTHONPATH
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


# Фикстура для тестового клиента FastAPI
@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def fake_db_session(mocker):
    return mocker.Mock(spec=Session)
