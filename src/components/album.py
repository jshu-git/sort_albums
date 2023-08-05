from pprint import pprint

from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth

from logging import getLogger

from time import sleep


class Album:
    def __init__(self, id, name, release_date):
        self.id = id
        self.name = name
        self.release_date = release_date

    def __repr__(self):
        return f"(id:{self.id}, name:{self.name}, release_date:{self.release_date})"


class AlbumSorter:
    def __init__(
        self,
        client_id,
        client_secret,
        redirect_uri="http://localhost:7777/callback",
        scope="user-library-read user-library-modify",
    ):
        self.log = getLogger()
        self.sp = Spotify(
            auth_manager=SpotifyOAuth(
                client_id=client_id,
                client_secret=client_secret,
                redirect_uri=redirect_uri,
                scope=scope,
            )
        )

    def save_albums(self, album_ids):
        for i in album_ids:
            self.sp.current_user_saved_albums_add(albums=[i])
            # this sleep is necessary. if you try to add them all immediately, spotify will sometimes mix up the order due to the async nature of the api
            sleep(1)

    def remove_albums(self, album_ids):
        for i in album_ids:
            self.sp.current_user_saved_albums_delete(albums=[i])

    def sort_albums(self, albums: list[Album], key):
        return sorted(albums, key=key)

    def get_saved_albums(self, offset=0):
        saved_albums = []
        while True:
            results = self.sp.current_user_saved_albums(limit=50, offset=offset)
            items = results["items"]

            # create Album objects and add to saved_albums
            saved_albums.extend(
                Album(
                    id=r["album"]["id"],
                    name=r["album"]["name"],
                    release_date=r["album"]["release_date"],
                )
                for r in items
            )

            if len(items) < 50:
                break
            offset += 50

        return saved_albums

    def is_sorted(self, albums: list[Album], key, desc=False):
        if desc:
            return all(
                key(albums[i]) >= key(albums[i + 1]) for i in range(len(albums) - 1)
            )
        else:
            return all(
                key(albums[i]) <= key(albums[i + 1]) for i in range(len(albums) - 1)
            )
