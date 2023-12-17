from tools.sorter import Sorter as AlbumSorter

if __name__ == "__main__":
    sorter = AlbumSorter()
    print(f'restoring album order from: {sorter.backup_path}')
    sorter.restore()
    print('restored!')
