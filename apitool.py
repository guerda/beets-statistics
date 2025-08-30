from fastapi import Response
from fastapi.staticfiles import StaticFiles

class StaticFilesCache(StaticFiles):
    def __init__(self, *args, cachecontrol: str, **kwargs):
        self.cachecontrol = cachecontrol
        super().__init__(*args, **kwargs)

    def file_response(self, *args, **kwargs) -> Response:
        resp: Response = super().file_response(*args, **kwargs)
        resp.headers.setdefault("Cache-Control", self.cachecontrol)
        return resp