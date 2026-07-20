FROM python:3.12

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

ENV PIP_DEFAULT_TIMEOUT=300
ENV POETRY_REQUESTS_TIMEOUT=300

# Install Poetry
RUN pip install --no-cache-dir poetry

# Copy dependency files first (better Docker cache)
COPY pyproject.toml poetry.lock ./

# Install dependencies into the system environment
RUN poetry config virtualenvs.create false \
    && poetry install --only main --no-root --no-interaction --no-ansi

# Copy the application source
COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]