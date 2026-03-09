FROM python:3.13-slim@sha256:8bc60ca09afaa8ea0d6d1220bde073bacfedd66a4bf8129cbdc8ef0e16c8a952
# Install uv.
COPY --from=ghcr.io/astral-sh/uv:0.10.9@sha256:10902f58a1606787602f303954cea099626a4adb02acbac4c69920fe9d278f82 /uv /uvx /bin/

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
