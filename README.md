# 🚀 FastAPI Users Microservice

Микросервис на FastAPI для работы с пользователями.  
Использует PostgreSQL, Alembic для миграций, Docker, Poetry и автозаполнение базы при старте.

---

## 📦 Стек технологий

- **FastAPI** — веб-фреймворк
- **PostgreSQL** — база данных
- **SQLAlchemy** — ORM
- **Alembic** — миграции
- **Pydantic v2** — валидация данных
- **Poetry** — управление зависимостями и окружением
- **Docker + Docker Compose** — контейнеризация

---

## 🚀 Быстрый старт

### 🔧 Требования

- [Poetry](https://python-poetry.org/docs/#installation)
- Docker
- Docker Compose
- Python 3.10+

---

### ▶️ Запуск проекта в Docker

```bash
docker-compose up --build
```
---

### Локальный запуск (без Docker)
# Установить зависимости
poetry install

# Активировать виртуальное окружение
poetry shell

# Применить миграции (если нужно)
poetry run alembic upgrade head

# Запустить приложение
poetry run uvicorn main:app --reload


### После старта

- 📌 API доступен по адресу: http://localhost:8000
- 📄 Swagger UI (документация): http://localhost:8000/docs
- 🔍 ReDoc (альтернативная документация): http://localhost:8000/redoc

---
### 🛠 Полезные команды
🔧 Работа с Docker

| Команда                              | Описание                          |
|--------------------------------------|-----------------------------------|
| `docker-compose up --build`         | Сборка и запуск проекта           |
| `docker-compose down`               | Остановка и удаление контейнеров  |
| `docker ps`                         | Список запущенных контейнеров     |
| `docker logs fastapi-app`          | Просмотр логов приложения         |
| `docker exec -it fastapi-app bash` | Войти внутрь контейнера           |

🔧 Работа с Poetry

| Команда                            | Описание                         |
|------------------------------------|----------------------------------|
| `poetry install`                  | Установить зависимости           |
| `poetry shell`                    | Войти в виртуальное окружение    |
| `poetry run <команда>`           | Выполнить команду в окружении    |
| `poetry add <пакет>`             | Добавить зависимость             |
| `poetry add --group dev <пакет>` | Добавить dev-зависимость         |
| `poetry env info --path` | Получить путь к окружению Poetry |
| `poetry run pytest` | Запустить тесты                  |