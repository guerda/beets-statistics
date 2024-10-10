# Beets statistics

## Intro

A neat music library is a great thing.
Wouldn't be insights on such a library be great?
With [beets](https://beets.io) you can manage and relate your music files to MusicBrainz IDs with all their great metadata.

What's this project, you can fire up a simple web page, which shows how many jazz albums you have, what the quality factor of your library is and how your top decade of music is.

In order to work, beets-statistics needs a beets library.

## What does beets-statistics look like?

Here's a couple of screenshot showing beets-statistics in action:



## How to run beets statistics?

### Run beets-statistics with Python

* Install Python 3.9 or higher
* Install `pipenv`
* Run `pipenv install` in the source directory
* Locate your beets library database
* Run `MUSICLIBRARY_DB="<path to db file>" pipenv run prod` to start the web app in production mode.
* Open the device's IP address on port 8000

### Run beets-statistics with Docker Compose

`docker-compose.yaml` 

Be sure to mount the musiclibrary.db in the volume section

```
services:
    beets-statistics:
        container_name: beets-statistics
        restart: always
        image: guerda/beets-statistics:0.0.1
        volumes:
            - /home/user/.beets/musiclibrary.db:/app/musiclibrary.db:ro
        ports:
            - 8000:8000
        environment:
            - MUSICLIBRARY_DB=/app/musiclibrary.db
```

## How to develop and/or contribute?

The development setup is pretty slim with `pipenv` and `ruff`.
Installing the necessary tools via `pipenv install --dev` gets you along.

You can start the web server in dev mode via
`pipenv run dev`
