# Beets statistics

## Intro

A well maintained music library is a great thing.
Wouldn't insights on such a library be great?
With [beets](https://beets.io) you can manage and relate your music files to MusicBrainz IDs with all their great metadata.

This project, _beets statistics_, offers a simple web page, which shows how many jazz albums you have, what the quality factor of your library is and what your top decade of music is.

In order to work, beets-statistics needs a beets library, so you should import all your music files with beets first.

## What does beets-statistics look like?

Here's a couple of screenshot showing beets-statistics in action:

| General statistics about the music library | Complete album list | Top genre list |
|-|-|-|
| ![Screenshot of a web page. Title is "Beets Statistics", then six navigation cards with "Home", "Albums", "Genres", "Artists", "Decades" and "Quality" are listed. Below a smaller headline "General insights". Then you see five cards in masonry layout with a purple to warm orange red gradient background. In white letters, the statistics are written on each of the cards: 9907 tracks, 1088 albums, 1 month, 1 days, 4 hours, 8 minutes and 10 seconds playback length, 60.5 GB disk usage and 134 BPM on average](img/screenshot-general-statistics.png) | ![Screenshot of a web page with nine cards in masonry layout. The cards have a greenish-mint background. Each card represents an album with the first line stating the album title in bold face, then the release year and the album artist. Last line shows the genre in italic style. Below the text, a green progress bar with a percentage is displayed. If the percentage is larger than 100%, the bar is red.](img/screenshot-albums.png) | ![Screenshot of a web page with headline "Genres". Below a table with two colums. The colums are titled "Genre" and "Number of albums". The first column contains Genres like Electronic, House, Rock, n/a, Punk Rock etc. The second colum shows green progress bars per row and the number of albums. The size of the progress bar represents the number of albums.](img/screenshot-genres.png) |

| Genre distribution | Bitrate distribution |
|-|-|
| ![Screenshot of a web page with a table with two colums. The columns are titled "Decade" and "Number of tracks". The decades listed are 0, 1960, 1970, until 2020 and 2930. The green progress bars per row are representing the number of tracks per decade in comparison to the total number of tracks. Largest bar is 5270 tracks in the 2000 decade.](img/screenshot-decades.png) | ![Screenshot of a web page with a table with two colums. The colums are titled "Bitrate [kbit/s]" and "Number of tracks". The bitrate buckets are listing bitrates from 1410 down to 160 kbit/s. The green progress bar represents the number of tracks in comparison to the total number of tracks. The largest progress bar is at 190 kbit/s with 1752 tracks.](img/screenshot-bitrate.png) | 


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
        image: ghcr.io/guerda/beets-statistics:0.0.1
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
