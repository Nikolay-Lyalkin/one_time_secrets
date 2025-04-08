FROM python:3.11.9

RUN pip install --no-cache-dir poetry

ENV POETRY_VIRTUALENVS_CREATE=false

WORKDIR /code

COPY pyproject.toml poetry.lock ./
RUN poetry install --no-root

COPY . .

CMD ["sh", "-c", "python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]