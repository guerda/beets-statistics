FROM python:3.11
WORKDIR /app
COPY ./Pipfile* /app/
RUN pip install pipenv
RUN pipenv install
COPY templates /app/templates/
COPY static /app/static/
COPY beetsstatistics.py app.py  /app
CMD ["pipenv", "run", "prod"]
