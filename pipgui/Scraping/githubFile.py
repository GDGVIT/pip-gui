import os


def EasyDir():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(current_dir, r"..\Resource_Files", 'Package Sources')


PKG_SOURCE_DIR = EasyDir()

os.system(f'curl https://github.com/vinta/awesome-python/blob/master/README.md >> {PKG_SOURCE_DIR}db.txt')
