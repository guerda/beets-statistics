import argparse
import os
import os.path
import sqlite3
from enum import Enum

import yaml

LOSSY_FORMATS = ["mp3", "aac", "ogg"]
LOSSLESS_FORMATS = ["flac", "wav"]


class DBNotFoundError(Exception):
    pass


class DBQueryError(Exception):
    pass


class Album:
    def __repr__(self):
        return f"ID: {self.id}, Title: {self.title}, Tracks: {self.tracks}/{self.track_total} ({self.complete_percentage}%), Album artist: {self.album_artist}, Genre: {self.genre}, Year: {self.year} ({self.original_year}), Album Art: {self.album_cover}"


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

    def convert_row_to_album(self, album):
        return_album = Album()
        return_album.id = album["album_id"]
        return_album.mb_albumid = album["mb_albumid"]
        return_album.title = album["album"]
        return_album.tracks = album["tracks"]
        return_album.track_total = album["tracktotal"]
        return_album.complete_percentage = album["complete"]
        return_album.album_artist = album["albumartist"]
        return_album.genre = album["genre"]
        return_album.year = album["year"]
        return_album.original_year = album["original_year"]
        return_album.barcode = album["barcode"]
        # id |artpath|added |albumartist |albumartist_sort|albumartist_credit|albumartists|albumartists_sort |albumartists_credit|album |genre |style|discogs_albumid|discogs_artistid|discogs_labelid|year|month|day|disctotal|comp|mb_albumid|mb_albumartistid|albumtype|albumtypes|label |barcode |mb_releasegroupid |release_group_title |asin|catalognum|script|language|country|albumstatus|albumdisambig|releasegroupdisambig|rg_album_gain|rg_album_peak|r128_album_gain|original_year|original_month|original_day|
        return return_album

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
            return_album = self.convert_row_to_album(album)

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
                            else ifnull(case when instr(a.genre, ';') then substr(a.genre, 0, instr(a.genre, ';')) else a.genre end , "n/a")
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
            if value is not None:
                return value[0]
            else:
                return None
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
            return results, lossless, lossy, unknown
        except sqlite3.Error as e:
            raise DBQueryError from e

    def get_track_decades(self):
        try:
            cursor = self.get_db_connection().cursor()
            query = """SELECT
                        i.YEAR / 10 * 10 as decade
                    FROM
                        items i
                    WHERE i.YEAR > 0;
                    """
            res = cursor.execute(query)
            results = res.fetchall()
            cursor.close()

            return results

        except sqlite3.Error as e:
            raise DBQueryError from e

    def get_track_quality(self):
        try:
            cursor = self.get_db_connection().cursor()
            query = """SELECT
                        bitrate / 1000 as bitrate
                    FROM
                        items i"""
            res = cursor.execute(query)
            results = res.fetchall()
            cursor.close()

            return results

        except sqlite3.Error as e:
            raise DBQueryError from e

    def get_genre_decade_heatmap(self):
        try:
            cursor = self.get_db_connection().cursor()
            query = """select 
                            case when instr(a.genre, ';') then substr(a.genre, 0, instr(a.genre, ';')) else a.genre end as genre,
                            YEAR / 10 * 10 as decade, 
                            count(1) as count
                        from albums a
                        where a.genre != '' and a.year > 0
                        group by 1,2 
                        order by 1,2 asc"""
            res = cursor.execute(query)
            results = res.fetchall()
            cursor.close()

            return results
        except sqlite3.Error as e:
            raise DBQueryError from e

    def get_album_cover_path(self, album_id: int):
        query = """select artpath from albums where id = {}""".format(album_id)
        path = self._query_one_value(query)

        if path and os.path.isfile(path):
            return path
        else:
            return None

    def get_added_timeline(self):
        try:
            cursor = self.get_db_connection().cursor()
            query = """select datetime(added, 'unixepoch') as added from items;"""
            cursor.execute(query)
            results = cursor.fetchall()
            cursor.close()
            return results
        except sqlite3.Error as e:
            raise DBQueryError from e

    def get_duplicates(self):
        try:
            cursor = self.get_db_connection().cursor()
            query = """SELECT
                          i2.mb_trackid, i2.title, i2.artist, i2.bitrate/1000 as bitrate, i2.album, i2.path
                       FROM items i2 where i2.mb_trackid in (select i1.mb_trackid from items i1
                        WHERE i1.mb_trackid <> ''
                        GROUP BY i1.mb_trackid
                       HAVING COUNT(*) > 1 )
                       ORDER BY i2.mb_trackid ASC;"""
            cursor.execute(query)
            results = cursor.fetchall()

            cursor.close()
            duplicates = []
            last_trackid = None
            duplicate_row = []

            for row in results:
                trackid = row["mb_trackid"]
                title = row["title"]
                artist = row["artist"]
                bitrate = row["bitrate"]
                album = row["album"]
                filename = row["path"]

                if trackid != last_trackid:
                    last_trackid = trackid
                    if len(duplicate_row) > 0:
                        duplicates.append(duplicate_row)
                        duplicate_row = []

                duplicate_entry = {
                    "trackid": trackid,
                    "artist": artist,
                    "title": title,
                    "album": album,
                    "bitrate": bitrate,
                    "filename": filename.decode("UTF-8"),
                }
                duplicate_row.append(duplicate_entry)

            if len(duplicate_row) > 0:
                duplicates.append(duplicate_row)

            return duplicates
        except sqlite3.Error as e:
            raise DBQueryError from e

    def get_items_not_in_mb(self):
        try:
            cursor = self.get_db_connection().cursor()
            query = """SELECT
                          i.title,
                          i.artist,
                          i.album
                       FROM
                          items i
                       WHERE i.mb_trackid = '';"""
            cursor.execute(query)
            results = cursor.fetchall()

            cursor.close()
            return results
        except sqlite3.Error as e:
            raise DBQueryError from e

    def get_albums_not_in_mb(self):
        try:
            cursor = self.get_db_connection().cursor()
            query = """SELECT
                          a.album,
                          a.albumartist
                       FROM
                          albums a
                       WHERE a.mb_albumid = '';"""
            cursor.execute(query)
            results = cursor.fetchall()

            cursor.close()
            return results
        except sqlite3.Error as e:
            raise DBQueryError from e

    def get_recently_added_albums(self):
        """
        Query and return the newest album added to the database.
        """
        try:
            cursor = self.get_db_connection().cursor()
            query = """select
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
                            i.album_id is not null and
                            a.album != ''
                        group by
                            i.album_id
                        order by a.added desc 
                        limit 10;"""
            cursor.execute(query)
            results = cursor.fetchall()

            cursor.close()

            result_albums = [self.convert_row_to_album(album) for album in results]

            return result_albums
        except sqlite3.Error as e:
            raise DBQueryError from e

    def get_worst_quality_tracks(self):
        try:
            cursor = self.get_db_connection().cursor()
            query = """select i.* from items i order by i.bitrate asc limit 10;"""
            cursor.execute(query)
            results = cursor.fetchall()

            cursor.close()

            return results
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
