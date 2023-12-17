from tools.sorter import Sorter as AlbumSorter

if __name__ == "__main__":
    sorter       = AlbumSorter()
    saved_albums = sorter.get_saved_albums()
    print('backing up...')
    sorter.backup(saved_albums)
    print('backed up!')
