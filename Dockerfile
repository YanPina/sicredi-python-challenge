FROM python:3.11-slim

WORKDIR /app

COPY pyproject.toml poetry.lock ./

# Instalar Poetry
RUN pip install --no-cache-dir poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-root --no-interaction --no-ansi

COPY . .

CMD ["python", "main.py"]
