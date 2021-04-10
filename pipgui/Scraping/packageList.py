import os
import json
import pkg_resources
from bs4 import BeautifulSoup


def EasyDir(folder):
    current_dir = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(current_dir, "../Resource_Files", folder)


def indices(string, substring):
    '''# Function to find both occurences of a tag'''
    return [string.find(substring), string.find(substring) + string[string.find(substring) + 1:].find(substring)]


PKG_SOURCE_DIR = EasyDir('Package Sources')
ASSETS_DIR = EasyDir('Assets')
PACKAGE_DIR = EasyDir('Current Packages')

# Source Code File
file = open(os.path.join(PKG_SOURCE_DIR, 'db.txt'), encoding="utf8")
src = str(file.read())
file.close()

# List of all Genres and their 'a' tag HREF values
genreList = json.load(open(os.path.join(PKG_SOURCE_DIR, 'genreListFile.json')))
genreTags = json.load(open(os.path.join(PKG_SOURCE_DIR, 'genreTagFile.json')))

# Genre and HREF value dictionary
genres = json.load(open(os.path.join(PKG_SOURCE_DIR, 'genreFile.json')))

# Tag values and their indices
indexDict = {i: max(indices(src, i)) for i in genreTags}


def substr(string, start, tag='ul'):
    sub = string[string[start:].find('<' + tag + '>')+start: string[start:].find(
        '</' + tag + '>') + start + len('</' + tag + '>')]
    aTags = BeautifulSoup(sub, 'html.parser').find_all('a')
    return [i.string for i in aTags]


# Dictionary of genre tags with all relative packages
packageDict = {i: substr(src, indexDict[i]) for i in genreTags}

json.dump(packageDict, open(os.path.join(
    PACKAGE_DIR + 'packageDictFile.json'), 'w'))

k = json.load(open(os.path.join(PACKAGE_DIR, 'packageDictFile.json')))
