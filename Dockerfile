FROM python:3.13-slim@sha256:1f3781f578e17958f55ada96c0a827bf279a11e10d6a458ecb8bde667afbb669
# Install uv.
COPY --from=ghcr.io/astral-sh/uv:latest@sha256:2320e6c239737dc73cccce393a8bb89eba2383d17018ee91a59773df802c20e6 /uv /uvx /bin/

WORKDIR /app
COPY ./uv.lock ./pyproject.toml /app/
RUN uv sync --frozen --no-cache
COPY templates /app/templates/
COPY static /app/static/
COPY beetsstatistics.py app.py apitool.py /app
CMD ["/app/.venv/bin/fastapi", "run", "app.py"]
