from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from beetsstatistics import AlbumSort, BeetsStatistics, DBNotFoundError, DBQueryError
import humanize
from fastapi import Depends
from typing import Annotated
from pydantic_settings import BaseSettings
from fastapi import HTTPException


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
    return templates.TemplateResponse(
        request=request, name="genres.html", context={"genres": genres}
    )


@app.get("/artists", response_class=HTMLResponse)
async def get_artist_stats(
    request: Request,
    beets_statistics: Annotated[BeetsStatistics, Depends(get_beets_statistics)],
):
    artists = beets_statistics.get_artist_stats(limit=100)
    count = beets_statistics.get_track_count()
    return templates.TemplateResponse(
        request=request, name="artists.html", context={"artists": artists, "track_count": count}
    )


@app.get("/decades", response_class=HTMLResponse)
async def get_track_decades(
    request: Request,
    beets_statistics: Annotated[BeetsStatistics, Depends(get_beets_statistics)],
):
    decades, count = beets_statistics.get_track_decades()
    return templates.TemplateResponse(
        request=request,
        name="decades.html",
        context={"decades": decades, "track_count": count},
    )


@app.get("/quality", response_class=HTMLResponse)
async def get_track_quality(
    request: Request,
    beets_statistics: Annotated[BeetsStatistics, Depends(get_beets_statistics)],
):
    bitrates, count = beets_statistics.get_track_quality(limit=20)
    return templates.TemplateResponse(
        request=request,
        name="quality.html",
        context={"bitrates": bitrates, "track_count": count},
    )
