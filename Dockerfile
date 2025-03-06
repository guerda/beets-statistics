FROM python:3.13
WORKDIR /app
COPY ./Pipfile* /app/
RUN pip install pipenv
RUN pipenv sync
COPY templates /app/templates/
COPY static /app/static/
COPY beetsstatistics.py app.py  /app
CMD ["pipenv", "run", "prod"]
