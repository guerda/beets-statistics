from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from main import AlbumSort
from main import BeetsStatistics

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

beets_statistics = BeetsStatistics("musiclibrary.db")


@app.get("/", response_class=HTMLResponse)
async def get_general_stats(request: Request):
    
    return templates.TemplateResponse(
        request=request, name="index.html"
    )



@app.get("/albums", response_class=HTMLResponse)
async def get_album_stats(request: Request, sort_by: AlbumSort = AlbumSort.ARTIST):
    albums = beets_statistics.get_albums_from_db(sort_by=sort_by)
    return templates.TemplateResponse(
        request=request, name="albums.html", context={"albums": albums}
    )


@app.get("/genres", response_class=HTMLResponse)
async def get_genre_count(request: Request):
    genres = beets_statistics.get_genre_count()
    return templates.TemplateResponse(
        request=request, name="genres.html", context={"genres": genres}
    )


@app.get("/artists", response_class=HTMLResponse)
async def get_artist_stats(request: Request):
    artists = beets_statistics.get_artist_stats()
    return templates.TemplateResponse(
        request=request, name="artists.html", context={"artists": artists}
    )
