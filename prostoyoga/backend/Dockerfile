FROM python:3.11-alpine AS builder
WORKDIR /tmp
RUN apk add build-base libffi-dev
RUN pip install poetry
COPY ./pyproject.toml ./poetry.lock ./
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

FROM python:3.11-alpine
WORKDIR /app
COPY --from=builder /tmp/requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY . .
EXPOSE 8088
CMD ["uvicorn", "src.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "8088"]
