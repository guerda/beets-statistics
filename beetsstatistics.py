import sqlite3
import yaml
import os
import argparse
import os.path
from enum import Enum

LOSSY_FORMATS = ["mp3", "aac", "ogg"]
LOSSLESS_FORMATS = ["flac", "wav"]


class DBNotFoundError(Exception):
    pass


class DBQueryError(Exception):
    pass


class Album:
    def __repr__(self):
        return f"ID: {self.id}, Title: {self.title}, Tracks: {self.tracks}/{self.track_total} ({self.complete_percentage}%), Album artist: {self.album_artist}, Genre: {self.genre}, Year: {self.year} ({self.original_year})"


class AlbumSort(Enum):
    ARTIST = "albumartist_sort"
    ALBUM = "album"
    YEAR = "year"


class BeetsStatistics:
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
            return os.path.expanduser(config[db_config_key])

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

    def get_albums_from_db(self, sort_by: AlbumSort = AlbumSort.ARTIST):
        connection = self.get_db_connection()
        cursor = connection.cursor()
        res = cursor.execute(
            """select
            i.album_id,
            i.album,
            count(i.track) as tracks,
            max(i.tracktotal) as tracktotal,
            ifnull(round(count(i.track)/ cast(max(i.tracktotal) as float), 2) * 100, 0) as complete,
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
        order by a.{} asc
        """.format(sort_by.value)
        )

        albums = res.fetchall()
        cursor.close()

        result = []
        for album in albums:
            return_album = Album()
            return_album.id = album["album_id"]
            return_album.title = album["album"]
            return_album.tracks = album["tracks"]
            return_album.track_total = album["tracktotal"]
            return_album.complete_percentage = album["complete"]
            return_album.album_artist = album["albumartist"]
            return_album.genre = album["genre"]
            return_album.year = album["year"]
            return_album.original_year = album["original_year"]
            # id |artpath|added |albumartist |albumartist_sort|albumartist_credit|albumartists|albumartists_sort |albumartists_credit|album |genre |style|discogs_albumid|discogs_artistid|discogs_labelid|year|month|day|disctotal|comp|mb_albumid|mb_albumartistid|albumtype|albumtypes|label |barcode |mb_releasegroupid |release_group_title |asin|catalognum|script|language|country|albumstatus|albumdisambig|releasegroupdisambig|rg_album_gain|rg_album_peak|r128_album_gain|original_year|original_month|original_day|

            result.append(return_album)
        return result

        """ By album
        """
    def get_genre_count(self, limit: int = 0):
        try:
            cursor = self.get_db_connection().cursor()
            res = cursor.execute(
                """select
                        case
                            when a.genre = '' then "n/a"
                            else ifnull(a.genre, "n/a")
                        end as genre,
                        count(1) as count
                    from
                        albums a
                    group by
                        a.genre
                    order by
                        2 desc
                    {}""".format("LIMIT {}".format(limit) if limit > 0 else "")
            )

            genres = res.fetchall()
            res = cursor.execute(
                """select
                        count(1)
                    from
                        albums"""
            )
            count = res.fetchone()[0]
            cursor.close()

            return genres, count
        except sqlite3.Error as e:
            raise DBQueryError from e

    def get_artist_stats(self, limit: int = 0):
        try:
            cursor = self.get_db_connection().cursor()
            res = cursor.execute(
                """select
                    count(1) as track_count,
                    i.artist
                from
                    items i
                group by
                    i.artist
                having
                    track_count > 1
                order by
                    1 desc,
                    i.artist_sort asc
                {}""".format("LIMIT {}".format(limit) if limit > 0 else "")
            )
            artists = res.fetchall()
            cursor.close()
            return artists
        except sqlite3.Error as e:
            raise DBQueryError from e

    def get_track_count(self):
        query = """select
              count(1) as count
              from
                  items"""
        track_count = self._query_one_value(query)
        return track_count

    def _query_one_value(self, query: str):
        try:
            cursor = self.get_db_connection().cursor()
            res = cursor.execute(query)
            value = res.fetchone()
            cursor.close()
            return value[0]
        except sqlite3.Error as e:
            raise DBQueryError from e

    def get_album_count(self):
        query = """select count(1) as count from albums"""
        return self._query_one_value(query)

    def get_playback_length(self):
        query = """SELECT sum(length) FROM items i"""
        return self._query_one_value(query)

    def get_file_size(self):
        query = """SELECT
                    sum(i.bitrate * i."length" / 8) AS SIZE
                FROM
                    items i;"""
        return self._query_one_value(query)

    def get_avg_bpm(self):
        query = """SELECT
                    round(avg(i.bpm))
                FROM
                    items i
                WHERE
                    i.bpm > 0"""
        return self._query_one_value(query)

    def map_file_format_to_lossy(self, formats):
        lossy = 0
        lossless = 0
        unknown = 0
        for file in formats:
            if file[0].lower() in LOSSLESS_FORMATS:
                lossless += file[1]
            elif file[0].lower() in LOSSY_FORMATS:
                lossy += file[1]
            else:
                unknown += file[1]
        return lossless, lossy, unknown

    def get_track_formats(self):
        try:
            cursor = self.get_db_connection().cursor()
            query = """SELECT
                        i.format,
                        count(1) AS count
                    FROM
                        items i
                    GROUP BY
                        i.format;"""
            res = cursor.execute(query)
            results = res.fetchall()
            cursor.close()
            lossless, lossy, unknown = self.map_file_format_to_lossy(results)
            print(
                "Lossless: {}, lossy: {}, unknown: {}".format(lossless, lossy, unknown)
            )
            return results, lossless, lossy, unknown
        except sqlite3.Error as e:
            raise DBQueryError from e

    def get_track_decades(self):
        try:
            cursor = self.get_db_connection().cursor()
            query = """SELECT
                        i.YEAR / 10 * 10 as decade,
                        count(1) AS count
                    FROM
                        items i
                    GROUP BY
                        1
                    ORDER BY
                        1 ASC;"""
            res = cursor.execute(query)
            results = res.fetchall()
            cursor.close()

            count = self._query_one_value("""SELECT count(1) from items i;""")
            return results, count

        except sqlite3.Error as e:
            raise DBQueryError from e

    def get_track_quality(self, limit: int = 0):
        try:
            cursor = self.get_db_connection().cursor()
            query = """SELECT
                        bitrate / 10000*10000 / 1000 as bitrate,
                        count(1) AS count
                    FROM
                        items i
                    GROUP BY
                        1
                    ORDER BY
                        1 desc
                    {}""".format("LIMIT {}".format(limit) if limit > 0 else "")
            res = cursor.execute(query)
            results = res.fetchall()
            cursor.close()

            count = self._query_one_value("""SELECT count(1) from items i;""")
            return results, count

        except sqlite3.Error as e:
            raise DBQueryError from e


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="beets-statistics")
    parser.add_argument("-d", "--beets-db", required=False)

    args = parser.parse_args()

    bs = BeetsStatistics(db_file=args.beets_db)
    print(bs.get_db_file_name())
    for album in bs.get_albums_from_db():
        print(album.title, album.complete_percentage)  # Complete percentage
    print("-" * 140)
    for artist in bs.get_artist_stats():
        print("{} - {}".format(artist["track_count"], artist["artist"]))

    bs.close()
