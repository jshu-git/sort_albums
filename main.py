from pprint       import pprint

from tools.sorter import Sorter as AlbumSorter

if __name__ == '__main__':
    '''
    This function sorts the user's saved Spotify albums by release date.
    It first gets all saved albums and makes a backup of the current order.
    It then sorts the albums by release date, removes the user's currently saved albums, and resaves them in the sorted order.
    '''
    sorter = AlbumSorter()

    # get saved albums
    saved_albums = sorter.get_saved_albums()

    # backup
    sorter.backup(saved_albums)
    print(f'backed up current album order to: {sorter.backup_path}')

    # check if already sorted
    if sorter.is_sorted(saved_albums, field='date'):
        print('albums already sorted')
        exit(0)

    input('about to sort albums. this will remove all your saved albums and then save them in sorted order. '
          'if you want to restore your current order with the above backup, run the restore.py script.\n'
          'press Enter to continue...')

    # sort by release date
    albums_sorted_by_date = sorter.sort_albums(saved_albums, field='date')

    # remove all
    sorter.remove_albums(albums_sorted_by_date)

    # re-save sorted albums
    sorter.save_albums(albums_sorted_by_date)

    # check if sorted
    if sorter.is_sorted(saved_albums, field='date'):
        print('sorted!')
    else:
        pprint(albums_sorted_by_date)
        raise Exception('not sorted, please try again')
