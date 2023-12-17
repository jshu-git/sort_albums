from tools.sorter import Sorter as AlbumSorter

if __name__ == "__main__":
    sorter = AlbumSorter()
    print(f'backing up current album order to {sorter.backup_path}')
    saved_albums = sorter.get_saved_albums()
    sorter.backup(saved_albums)
    print(f'backed up to {sorter.backup_path}')
