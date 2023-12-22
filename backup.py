from tools.sorter import Sorter as AlbumSorter

if __name__ == "__main__":
    sorter = AlbumSorter()
    saved_albums = sorter.get_saved_albums()
    sorter.backup(saved_albums)
    print(f'backed up current album order to: {sorter.backup_path}')
