FROM python:3.9
WORKDIR /app
COPY ./Pipfile* /app/
RUN pip install pipenv
RUN pipenv install
COPY templates /app/templates/
COPY static /app/static/
COPY main.py app.py  /app
CMD ["pipenv", "run", "prod"]