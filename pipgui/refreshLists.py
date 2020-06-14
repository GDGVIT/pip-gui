import logging
class refreshList(object):

    """ This class is for refreshing list of packages and loading them in the interface """

    def __init__(self):

        print('\nRefreshing Online Package List... ')
        try:
            from pipgui.Scraping import pypiList
        except Exception as e:
            print('Unable to update package list!')
            
        print("\nRefreshing Installed Package List...")
        try:
            from pipgui.Package_Management import installedList
        except Exception as e:
            # logging.error('Unable to fetch installed packages!')
            print('Unable to update install list!')
            
        print("\nRefreshing Outdated Package List...")
        try:
            from pipgui.Package_Management import outdatedList
        except Exception as e:
            print('Unable to update outdated list!')


if __name__ == '__main__':
    refreshList()
