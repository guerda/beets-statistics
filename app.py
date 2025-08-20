import logging
from typing import Annotated
from urllib.parse import quote_plus

import humanize
from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic_settings import BaseSettings

from beetsstatistics import AlbumSort, BeetsStatistics, DBNotFoundError, DBQueryError

logger = logging.getLogger("uvicorn.error")


class InitializationError(Exception):
    pass


class Settings(BaseSettings):
    musiclibrary_db: str


beets_statistics = None


async def get_beets_statistics():
    global beets_statistics
    try:
        beets_statistics = BeetsStatistics(settings.musiclibrary_db)
        if beets_statistics.get_db_connection() is None:
            raise InitializationError("Could not get access database file.")
    except (DBNotFoundError, DBQueryError) as e:
        raise HTTPException(
            status_code=500,
            detail="Could not find find or access database file: {}".format(e),
        )
    try:
        yield beets_statistics
    finally:
        beets_statistics.close()


settings = Settings()
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")
templates.env.filters["quote_plus"] = lambda u: quote_plus(u)


@app.get("/", response_class=HTMLResponse)
async def get_general_stats(
    request: Request,
    beets_statistics: Annotated[BeetsStatistics, Depends(get_beets_statistics)],
):
    try:
        track_count = beets_statistics.get_track_count()
        album_count = beets_statistics.get_album_count()
        playback_length = beets_statistics.get_playback_length()
        playback_length_str = humanize.precisedelta(playback_length)

        file_size_str = humanize.naturalsize(beets_statistics.get_file_size())
        avg_bpm = beets_statistics.get_avg_bpm()
        format_count, lossless, lossy, unknown = beets_statistics.get_track_formats()

        recently_added_albums = beets_statistics.get_recently_added_albums()
    except (DBQueryError, DBNotFoundError) as e:
        raise HTTPException(
            status_code=500, detail="Could not query general statistics: {}".format(e)
        )
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "track_count": track_count,
            "album_count": album_count,
            "playback_length": playback_length_str,
            "file_size": file_size_str,
            "avg_bpm": avg_bpm,
            "format_count": format_count,
            "lossless": lossless,
            "lossy": lossy,
            "unknown": unknown,
            "recently_added_albums": recently_added_albums
        },
    )


@app.get("/albums", response_class=HTMLResponse)
async def get_album_stats(
    request: Request,
    beets_statistics: Annotated[BeetsStatistics, Depends(get_beets_statistics)],
    sort_by: AlbumSort = AlbumSort.ARTIST,
):
    albums = beets_statistics.get_albums_from_db(sort_by=sort_by)
    return templates.TemplateResponse(
        request=request, name="albums.html", context={"albums": albums}
    )


@app.get("/genres", response_class=HTMLResponse)
async def get_genre_count(
    request: Request,
    beets_statistics: Annotated[BeetsStatistics, Depends(get_beets_statistics)],
):
    genres = beets_statistics.get_genre_count(limit=20)
    genre_list = []
    count_list = []
    for genre in genres[0]:
        genre_list.append(genre["genre"])
        count_list.append(genre["count"])
    return templates.TemplateResponse(
        request=request,
        name="genres.html",
        context={"genres": genres, "genre_list": genre_list, "count_list": count_list},
    )


@app.get("/artists", response_class=HTMLResponse)
async def get_artist_stats(
    request: Request,
    beets_statistics: Annotated[BeetsStatistics, Depends(get_beets_statistics)],
):
    artists = beets_statistics.get_artist_stats(limit=100)
    artist_list = []
    count_list = []
    for artist in artists:
        artist_list.append(artist["artist"])
        count_list.append(artist["track_count"])
    count = beets_statistics.get_track_count()
    return templates.TemplateResponse(
        request=request,
        name="artists.html",
        context={
            "artists": artists,
            "track_count": count,
            "artist_list": artist_list,
            "count_list": count_list,
        },
    )


@app.get("/decades", response_class=HTMLResponse)
async def get_track_decades(
    request: Request,
    beets_statistics: Annotated[BeetsStatistics, Depends(get_beets_statistics)],
):
    decades = beets_statistics.get_track_decades()
    return templates.TemplateResponse(
        request=request,
        name="decades.html",
        context={"decades": decades},
    )


@app.get("/quality", response_class=HTMLResponse)
async def get_track_quality(
    request: Request,
    beets_statistics: Annotated[BeetsStatistics, Depends(get_beets_statistics)],
):
    bitrates = beets_statistics.get_track_quality()
    return templates.TemplateResponse(
        request=request,
        name="quality.html",
        context={"bitrates": bitrates},
    )


@app.get("/genre-decade-heatmap", response_class=HTMLResponse)
async def get_genre_decade_heatmap(
    request: Request,
    beets_statistics: Annotated[BeetsStatistics, Depends(get_beets_statistics)],
):
    results = beets_statistics.get_genre_decade_heatmap()

    min_decade = 9999
    max_decade = 0

    heatmap = {}
    genre_list = []

    for result in results:
        decade = result["decade"]
        count = result["count"]
        genre = result["genre"]

        if genre not in genre_list:
            genre_list.append(genre)

        min_decade = min(min_decade, decade)
        max_decade = max(max_decade, decade)

        if genre not in heatmap:
            heatmap[genre] = {}

        heatmap[genre][decade] = count

    # Fill out sparse table
    for genre in heatmap:
        for decade in range(min_decade, max_decade + 1, 10):
            if decade not in heatmap[genre]:
                heatmap[genre][decade] = 0

    # Sort z values per genre
    for genre in heatmap:
        sorted_genre = dict(sorted(heatmap[genre].items()))
        heatmap[genre] = sorted_genre

    return templates.TemplateResponse(
        request=request,
        name="genre-decade-heatmap.html",
        context={
            "heatmap": heatmap,
            "decades": range(min_decade, max_decade + 1, 10),
            "genre_list": genre_list,
        },
    )


@app.get("/cover/{album_id}", response_class=FileResponse)
async def get_album_cover(
    album_id: str,
    beets_statistics: Annotated[BeetsStatistics, Depends(get_beets_statistics)],
):
    album_cover_path = beets_statistics.get_album_cover_path(album_id)
    if album_cover_path is None:
        album_cover_path = "static/blank.png"
    return album_cover_path


@app.get("/added-timeline", response_class=HTMLResponse)
async def get_added_timeline(
    request: Request,
    beets_statistics: Annotated[BeetsStatistics, Depends(get_beets_statistics)],
):
    timeline = beets_statistics.get_added_timeline()
    return templates.TemplateResponse(
        request=request,
        name="added-timeline.html",
        context={"timeline": timeline},
    )


@app.get("/duplicates", response_class=HTMLResponse)
async def get_duplicates(
    request: Request,
    beets_statistics: Annotated[BeetsStatistics, Depends(get_beets_statistics)],
):
    duplicates = beets_statistics.get_duplicates()

    return templates.TemplateResponse(
        request=request, name="duplicates.html", context={"duplicates": duplicates}
    )


@app.get("/not-in-mb", response_class=HTMLResponse)
async def get_not_in_mb(
    request: Request,
    beets_statistics: Annotated[BeetsStatistics, Depends(get_beets_statistics)],
):
    items_not_in_mb = beets_statistics.get_items_not_in_mb()
    albums_not_in_mb = beets_statistics.get_albums_not_in_mb()

    return templates.TemplateResponse(
        request=request,
        name="not-in-mb.html",
        context={"tracks": items_not_in_mb, "albums": albums_not_in_mb},
    )
