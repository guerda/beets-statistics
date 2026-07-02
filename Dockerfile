FROM python:3.14.6-slim@sha256:b877e50bd90de10af8d82c57a022fc2e0dc731c5320d762a27986facfc3355c1
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
