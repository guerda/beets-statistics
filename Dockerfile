FROM python:3.13-slim@sha256:1f3781f578e17958f55ada96c0a827bf279a11e10d6a458ecb8bde667afbb669
# Install uv.
COPY --from=ghcr.io/astral-sh/uv:latest@sha256:9a23023be68b2ed09750ae636228e903a54a05ea56ed03a934d00fe9fbeded4b /uv /uvx /bin/

WORKDIR /app
COPY ./uv.lock ./pyproject.toml /app/
RUN uv sync --frozen --no-cache
COPY templates /app/templates/
COPY static /app/static/
COPY beetsstatistics.py app.py apitool.py /app
CMD ["/app/.venv/bin/fastapi", "run", "app.py"]
