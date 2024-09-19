### Docker

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