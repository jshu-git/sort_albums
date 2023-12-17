from time           import sleep
from os             import environ
from json           import dump, load

from spotipy        import Spotify
from spotipy.oauth2 import SpotifyOAuth

# tools
from .album         import Album

class Sorter:
    def __init__(self, backup_path='backup.json'):
        auth             = SpotifyOAuth(client_id     = environ.get('CLIENT_ID'),
                                        client_secret = environ.get('CLIENT_SECRET'),
                                        redirect_uri  = 'http://localhost:7777/callback',
                                        scope         = 'user-library-read user-library-modify')
        self.sp          = Spotify(auth_manager=auth)
        self.backup_path = backup_path

    # entry points
    def backup(self, albums):
        '''
        This function backs up the given albums to a local JSON file.
        '''
        albums_sorted_by_added_at = self.sort_albums(albums=albums, field='added_at')
        albums_as_dict            = [album.to_dict() for album in albums_sorted_by_added_at]

        with open(self.backup_path, 'w') as f:
            dump(albums_as_dict, f, indent=4)

    def restore(self):
        '''
        This function saves albums to the user's library by reading a local JSON file.
        '''
        with open(self.backup_path, 'r') as f:
            album_data = load(f)
        albums = [Album(**data) for data in album_data]

        self.remove_albums(albums)
        self.save_albums(albums)

    # api
    def get_saved_albums(self):
        '''
        This function gets all of the user's saved albums and creates Album objects.
        '''
        offset = 0
        saved  = []
        while True:
            results = self.sp.current_user_saved_albums(limit=50, offset=offset)
            items   = results['items']

            # create Album objects
            saved.extend(
                Album(
                    id       = r['album']['id'],
                    name     = r['album']['name'],
                    date     = r['album']['release_date'],
                    added_at = r['added_at']
                )
                for r in items
            )
            if len(items) < 50:
                break
            offset += 50
        return saved

    def remove_albums(self, albums):
        '''
        This function removes the given albums from the user's library. It removes 50 at a time due to an API limit.
        '''
        offset = 50
        ids    = [album.id for album in albums]
        while len(ids) > 0:
            self.sp.current_user_saved_albums_delete(albums=ids[:offset])
            ids = ids[offset:]

    def save_albums(self, albums):
        '''
        This function saves the given albums to the user's library.
        It saves 1 at a time with a delay due to the API mixing up the order if you save them all at once.
        '''
        ids = [album.id for album in albums]
        for i in ids:
            self.sp.current_user_saved_albums_add(albums=[i])
            sleep(1)

    # helpers
    def sort_albums(self, albums, field):
        return sorted(albums, key=self._get_key_from_field(field))

    def is_sorted(self, albums, field):
        key = self._get_key_from_field(field)
        return all(key(albums[i]) >= key(albums[i + 1]) for i in range(len(albums) - 1))

    def _get_key_from_field(self, field):
        if field == 'date':
            return lambda album: album.date
        elif field == 'added_at':
            return lambda album: album.added_at
        else:
            raise ValueError(f"invalid field '{field}'")
