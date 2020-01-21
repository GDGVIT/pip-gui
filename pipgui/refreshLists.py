import logging


class refreshList(object):

    """This class is for refreshing list of packages and loading them in the interface"""

    def __init__(self):

        print('\nRefreshing Online Package List... ')
        try:
            from Scraping import pypiList
        except Exception as e:
            logging.error('Unable to fetch the online packages!')
        print("\nRefreshing Installed Package List...")
        try:
            from Package_Management import installedList
        except Exception as e:
            logging.error('Unable to fetch installed packages!')
        print("\nRefreshing Outdated Package List...")
        try:
            from Package_Management import outdatedList

        except Exception as e:
            logging.error('Unable to update outdated list!')


if __name__ == '__main__':
    refreshList()
