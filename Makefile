.PHONY: all fmt test changelog

all: fmt test

fmt:
	ruff format
	ruff check --fix


test:
	pytest


changelog:
	git-cliff -O CHANGELOG.md