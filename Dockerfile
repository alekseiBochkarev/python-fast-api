FROM python:3.10-slim

WORKDIR /app

# Устанавливаем netcat
RUN apt-get update && apt-get install -y netcat-openbsd && apt-get clean

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем всё в /app
COPY . .

RUN chmod +x /app/entrypoint.sh

# Запускаем скрипт
CMD ["/app/entrypoint.sh"]
