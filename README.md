# Beets statistics

## Intro

A well maintained music library is a great thing.
Wouldn't insights on such a library be great?
With [beets](https://beets.io) you can manage and relate your music files to MusicBrainz IDs with all their great metadata.

This project, _beets statistics_, offers a simple web page, which shows how many jazz albums you have, what the quality factor of your library is and what your top decade of music is.

In order to work, beets-statistics needs a beets library, so you should import all your music files with beets first.

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

If you have a correction or an issue, open an issue here or contact me directly.
A PR in a separater branch in your fork goes a long way, so feel free to open it up.


# License

This project is licensed under GNU GPL 3.0.
