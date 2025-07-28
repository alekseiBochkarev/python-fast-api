#!/bin/bash

echo "⏳ Ждём PostgreSQL..."
while ! nc -z db 5432; do
  sleep 1
done

echo "✅ PostgreSQL доступен!"
echo "⚙️ Выполняем миграции..."
alembic upgrade head

echo "🌱 Заполняем базу пользователями..."
python -m data.seed_users  # УБРАЛ "app/" — ты уже в /app

echo "🚀 Запускаем FastAPI..."
uvicorn main:app --host 0.0.0.0 --port 8000  # УБРАЛ "app." — ты уже в /app