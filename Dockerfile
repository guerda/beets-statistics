FROM python:3.13-slim@sha256:739e7213785e88c0f702dcdc12c0973afcbd606dbf021a589cab77d6b00b579d
# Install uv.
COPY --from=ghcr.io/astral-sh/uv:0.11.3@sha256:90bbb3c16635e9627f49eec6539f956d70746c409209041800a0280b93152823 /uv /uvx /bin/

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
