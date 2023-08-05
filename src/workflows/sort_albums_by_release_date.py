from ..components.album import AlbumSorter

from pprint import pprint


def sort_albums_by_release_date():
    sorter = AlbumSorter(
        client_id="",
        client_secret="",
    )

    # get all saved albums
    saved_albums = sorter.get_saved_albums()
    sorted = sorter.is_sorted(
        albums=saved_albums, key=lambda album: album.release_date, desc=True
    )
    if sorted:
        print("already sorted")
        return

    # sort by release date
    sorted_albums = sorter.sort_albums(
        saved_albums, key=lambda album: album.release_date
    )
    # pprint(sorted_albums)
    album_ids = [album.id for album in sorted_albums]

    # unfavorite all
    sorter.remove_albums(album_ids)

    # resave sorted albums
    sorter.save_albums(album_ids)

    # test if sorted
    # sorted = sorter.is_sorted(
    #     albums=sorter.get_saved_albums(), key=lambda album: album.release_date, desc=True
    # )
    # print(f"Sorted: {sorted}")


if __name__ == "__main__":
    sort_albums_by_release_date()
