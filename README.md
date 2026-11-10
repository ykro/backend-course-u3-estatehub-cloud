# EstateHub Cloud API

API inmobiliaria con autenticación JWT, autorización por propietario y despliegue en Google Cloud Run.

## Unidad 3

Plantilla de la Unidad 3 del curso.

## Requisitos

- [uv](https://docs.astral.sh/uv/), que instala Python 3.13 y las dependencias exactas de `uv.lock`.

## Instalar y correr

```bash
uv sync
cp .env.example .env
uv run python -c "import secrets; print(secrets.token_urlsafe(48))"   # pega el resultado en JWT_SECRET_KEY de .env
uv run uvicorn app.main:app --reload
```

La consola queda en http://127.0.0.1:8000 y Swagger en `/docs`.
Sin un `JWT_SECRET_KEY` válido la app no arranca; es intencional.

## Tests

```bash
uv run pytest -v                  # solo los tests
uv run ruff check . && uv run ruff format --check . && uv run pytest -v   # chequeo completo
```

El archivo `AGENTS.md` trae las reglas para el asistente de IA.

El enunciado del reto, la rúbrica y la guía paso a paso están en el curso.
