FROM python:3.13-slim@sha256:a0779d7c12fc20be6ec6b4ddc901a4fd7657b8a6bc9def9d3fde89ed5efe0a3d
# Install uv.
COPY --from=ghcr.io/astral-sh/uv:0.11.6@sha256:b1e699368d24c57cda93c338a57a8c5a119009ba809305cc8e86986d4a006754 /uv /uvx /bin/

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
