import sqlite3
import yaml
import os
import musicbrainzngs as mb
from pprint import pprint 

def get_db_file_name():
    db_config_key = "library"
    config_file_name = os.path.expanduser("~/.config/beets/config.yaml")
    with open(config_file_name, "r") as file:
        config = yaml.safe_load(file)
        return config[db_config_key]

def get_track_count(artist: str, album: str):
    mb.set_useragent("beets-statistics", 0.1)
    albums = mb.search_releases(artist=artist, release=album, limit=5)
    print(albums["release-count"])
    for album in albums["release-list"]:
        pprint(album, width=200)
        print("-"*200)


if __name__ == "__main__":
    print(get_db_file_name())
    print(get_track_count(artist="Deichkind", album="Neues vom Dauerzustand"))
