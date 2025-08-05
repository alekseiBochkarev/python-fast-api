FROM python:3.10-slim

# Установим Poetry
RUN pip install poetry

WORKDIR /app

RUN apt-get update && apt-get install -y netcat-openbsd && apt-get clean

# Скопируем только файлы зависимостей
COPY pyproject.toml poetry.lock ./
COPY README.md .

# Установим зависимости без виртуального окружения
RUN poetry config virtualenvs.create false \
    && poetry install --no-root --no-interaction --no-ansi

# Копируем остальной код в /app
COPY . .


RUN chmod +x /app/entrypoint.sh

# Запускаем скрипт
CMD ["/app/entrypoint.sh"]
