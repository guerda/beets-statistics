from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from main import AlbumSort
from main import BeetsStatistics
import humanize

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

beets_statistics = BeetsStatistics("musiclibrary.db")


@app.get("/", response_class=HTMLResponse)
async def get_general_stats(request: Request):
    track_count = beets_statistics.get_track_count()
    album_count = beets_statistics.get_album_count()
    playback_length = beets_statistics.get_playback_length()
    playback_length_str = humanize.naturaldelta(playback_length)
    
    file_size_str = humanize.naturalsize(beets_statistics.get_file_size())
    avg_bpm = beets_statistics.get_avg_bpm()

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "track_count": track_count,
            "album_count": album_count,
            "playback_length": playback_length_str,
            "file_size": file_size_str,
            "avg_bpm": avg_bpm
        },
    )


@app.get("/albums", response_class=HTMLResponse)
async def get_album_stats(request: Request, sort_by: AlbumSort = AlbumSort.ARTIST):
    albums = beets_statistics.get_albums_from_db(sort_by=sort_by)
    return templates.TemplateResponse(
        request=request, name="albums.html", context={"albums": albums}
    )


@app.get("/genres", response_class=HTMLResponse)
async def get_genre_count(request: Request):
    genres = beets_statistics.get_genre_count(limit=20)
    return templates.TemplateResponse(
        request=request, name="genres.html", context={"genres": genres}
    )


@app.get("/artists", response_class=HTMLResponse)
async def get_artist_stats(request: Request):
    artists = beets_statistics.get_artist_stats(limit=100)
    return templates.TemplateResponse(
        request=request, name="artists.html", context={"artists": artists}
    )
