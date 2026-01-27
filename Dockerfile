FROM python:3.13-slim@sha256:51e1a0a317fdb6e170dc791bbeae63fac5272c82f43958ef74a34e170c6f8b18
# Install uv.
COPY --from=ghcr.io/astral-sh/uv:0.9.27@sha256:143b40f4ab56a780f43377604702107b5a35f83a4453daf1e4be691358718a6a /uv /uvx /bin/

WORKDIR /app
COPY ./uv.lock ./pyproject.toml /app/

# Disable development dependencies
ENV UV_NO_DEV=1
ENV UV_COMPILE_BYTECODE=1

RUN uv sync --frozen --no-cache
COPY templates /app/templates/
COPY static /app/static/
COPY beetsstatistics.py app.py apitool.py /app
CMD ["/app/.venv/bin/fastapi", "run", "app.py"]
