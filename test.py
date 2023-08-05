from pprint import pprint
from operator import itemgetter

from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth

# creds credentials
sp = Spotify(
    auth_manager=SpotifyOAuth(
        client_id="",
        client_secret="",
        redirect_uri="http://localhost:7777/callback",
        scope="user-library-read user-library-modify",
    )
)

# get all favorited
offset = 0
favorited_albums = []
while True:
    results = sp.current_user_saved_albums(limit=50, offset=offset)
    favorited_albums.extend(results["items"])
    if len(results["items"]) < 50:
        break
    offset += 50

# extract release date and store in a list
albums_with_release_date = [
    (album["album"]["id"], album["album"]["name"], album["album"]["release_date"])
    for album in favorited_albums
]
# pprint(albums_with_release_date)

# sort by release date
sorted_albums = sorted(albums_with_release_date, key=itemgetter(2))
pprint(sorted_albums)

# unfavorite all
album_ids = [album[0] for album in albums_with_release_date]
for i in range(0, len(album_ids), 50):
    sp.current_user_saved_albums_delete(albums=album_ids[i : i + 50])

# refavorite sorted albums
for album_id in [album[0] for album in sorted_albums]:
    sp.current_user_saved_albums_add(albums=[album_id])
