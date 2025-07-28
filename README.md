# 🚀 FastAPI Users Microservice

Микросервис на FastAPI для работы с пользователями.  
Использует PostgreSQL, Alembic для миграций, Docker и автозаполнение базы при старте.

---

## 📦 Стек технологий

- **FastAPI** — веб-фреймворк
- **PostgreSQL** — база данных
- **SQLAlchemy** — ORM
- **Alembic** — миграции
- **Docker + Docker Compose** — контейнеризация
- **Pydantic v2** — валидация данных

---

## 🚀 Быстрый старт

### 🔧 Требования

- Docker
- Docker Compose

### ▶️ Запуск проекта

```bash
docker-compose up --build
```
---

### После старта

- 📌 API доступен по адресу: http://localhost:8000
- 📄 Swagger UI (документация): http://localhost:8000/docs
- 🔍 ReDoc (альтернативная документация): http://localhost:8000/redoc

---
### 🛠 Полезные команды
🔧 Работа с Docker

- Команда — Описание
- docker-compose up --build — Сборка и запуск проекта
- docker-compose down —	        Остановка и удаление контейнеров
- docker ps	— Список запущенных контейнеров
- docker logs fastapi-app —	Просмотр логов приложения
- docker exec -it fastapi-app bash —	Войти внутрь контейнера
