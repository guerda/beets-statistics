FROM python:3.13-slim
# Install uv.
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app
COPY ./uv.lock ./pyproject.toml /app/
RUN uv sync --frozen --no-cache
COPY templates /app/templates/
COPY static /app/static/
COPY beetsstatistics.py app.py  /app
CMD ["/app/.venv/bin/fastapi", "run", "app.py"]
