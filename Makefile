.PHONY: all fmt qa deps test changelog

server: dev caddy

all: fmt qa  deps test

fmt:
	ruff format
	ruff check --fix

qa:
	ruff check
	ty check

deps:
	pip-audit

test:
	pytest

dev:
	MUSICLIBRARY_DB=musiclibrary.db LOG_LEVEL=debug MEDIA_PATH=/home/philip/Musik fastapi dev app.py --host 0.0.0.0

caddy:
	caddy start &

prod:
	fastapi run app.py

changelog:
	git-cliff -o CHANGELOG.md
