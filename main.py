import sqlite3
import yaml
import os
import musicbrainzngs as mb
from pprint import pprint 
import argparse
import os.path
    

class DBNotFoundError(Exception):
    pass

class Album():
    def __repr__(self):
        return f"ID: {self.id}, Title: {self.title}, Tracks: {self.tracks}/{self.track_total} ({self.complete_percentage}%), Album artist: {self.album_artist}, Genre: {self.genre}, Year: {self.year} ({self.original_year})"

class BeetsStatistics():

    def __init__(self, db_file: str):
        self.db_file = db_file
        self.connection = None
    


    def get_db_file_name(self):
        if self.db_file is not None:
            return self.db_file
        db_config_key = "library"
        # TODO Catch exception if file does not exist
        config_file_name = os.path.expanduser("~/.config/beets/config.yaml")
        with open(config_file_name, "r") as file:
            config = yaml.safe_load(file)
            return config[db_config_key]

    def get_track_count_from_mb(self, artist: str, album: str):
        mb.set_useragent("beets-statistics", 0.1)
        albums = mb.search_releases(artist=artist, release=album, limit=5)
        print(albums["release-count"])
        for album in albums["release-list"]:
            pprint(album, width=200)
            print("-"*200)

    def get_db_connection(self):
        if self.connection is not None:
            return self.connection

        db_file_name = self.get_db_file_name()
        if not db_file_name:
            raise DBNotFoundError
        
        if not os.path.isfile(db_file_name):
            raise DBNotFoundError(db_file_name)
        self.connection = sqlite3.connect(db_file_name)
        # Set row factory so that named dicts are returned
        self.connection.row_factory = sqlite3.Row
        return self.connection

    def close(self):
        if self.connection:
            self.connection.close()

    def get_albums_from_db(self):
        connection = self.get_db_connection()
        cursor = connection.cursor()
        res = cursor.execute("""select
            i.album_id,
            i.album,
            count(i.track) as tracks,
            max(i.tracktotal) as tracktotal,
            round(count(i.track)/ cast(max(i.tracktotal) as float), 2) * 100 as complete,
            a.*
        from
            albums a
        left join
            items i on
            i.album_id = a.id
        where
            album_id is not null
        group by
            i.album_id
        """)

        albums = res.fetchall()
        cursor.close()

        result = []
        for album in albums:
            return_album = Album()
            return_album.id = album["album_id"]
            return_album.title = album["album"]
            return_album.tracks = album["tracks"]
            return_album.track_total  = album["tracktotal"]
            return_album.complete_percentage = album["complete"]
            return_album.album_artist = album["albumartist"]
            return_album.genre = album["genre"]
            return_album.year = album["year"]
            return_album.original_year = album["original_year"]
            # id |artpath|added |albumartist |albumartist_sort|albumartist_credit|albumartists|albumartists_sort |albumartists_credit|album |genre |style|discogs_albumid|discogs_artistid|discogs_labelid|year|month|day|disctotal|comp|mb_albumid|mb_albumartistid|albumtype|albumtypes|label |barcode |mb_releasegroupid |release_group_title |asin|catalognum|script|language|country|albumstatus|albumdisambig|releasegroupdisambig|rg_album_gain|rg_album_peak|r128_album_gain|original_year|original_month|original_day|
        
            result.append(return_album)
        return result

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="beets-statistics")
    parser.add_argument("-d", "--beets-db", required=False)

    args = parser.parse_args()


    bs = BeetsStatistics(db_file=args.beets_db)
    print(bs.get_db_file_name())
    for album in bs.get_albums_from_db():
        print(album.title, album.complete_percentage) # Complete percentage
    bs.close()
