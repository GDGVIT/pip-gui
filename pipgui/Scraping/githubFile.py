import os

PKG_SOURCE_DIR = '../Resource_Files/Package Sources/'

os.system(f'curl https://github.com/vinta/awesome-python/blob/master/README.md >> {PKG_SOURCE_DIR}db.txt')
