from tools.sorter import Sorter as AlbumSorter

if __name__ == "__main__":
    sorter = AlbumSorter()
    print('restoring...')
    sorter.restore()
    print('restored!')
