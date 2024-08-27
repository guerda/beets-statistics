from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from main import BeetsStatistics

app = FastAPI()
templates = Jinja2Templates(directory="templates")

beets_statistics = BeetsStatistics("musiclibrary.db")

albums = beets_statistics.get_albums_from_db()


@app.get("/", response_class=HTMLResponse)
async def get_album_stats(request: Request):
    print(len(albums))
    return templates.TemplateResponse(request=request, name="index.html", context={"albums": albums})