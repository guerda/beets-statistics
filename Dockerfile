FROM python:3.14.7-slim@sha256:cad9a2c871761c413caa6fdd6441c783451e740a48aaeba60ae62a8b53525ef6
# Install uv.
COPY --from=ghcr.io/astral-sh/uv:0.11.6@sha256:b1e699368d24c57cda93c338a57a8c5a119009ba809305cc8e86986d4a006754 /uv /uvx /bin/

WORKDIR /app
COPY ./uv.lock ./pyproject.toml /app/

# Disable development dependencies
ENV UV_NO_DEV=1
ENV UV_COMPILE_BYTECODE=1
ENV MUSICLIBRARY_DB=/root/.beets/musiclibrary.db
ENV MEDIA_PATH=/media/music

RUN uv sync --frozen --no-cache
COPY templates /app/templates/
COPY static /app/static/
COPY *.py /app
CMD ["/app/.venv/bin/fastapi", "run", "app.py"]
