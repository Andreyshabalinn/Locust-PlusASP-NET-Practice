# Используем Python
FROM python:3.10-slim

# Устанавливаем зависимости
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем скрипт Locust
COPY locustfile.py .

# Устанавливаем порт для Locust UI
EXPOSE 8089

# Указываем команду запуска
ENTRYPOINT ["locust", "-f", "locustfile.py"]
