import os
import re
import json
from bs4 import BeautifulSoup


def EasyDir():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(current_dir, r"..\Resource_Files", 'Package Sources')


PKG_SOURCE_DIR = EasyDir()

genrePattern = re.compile(r'#[\w-]+')

# Source Code File
file = open(os.path.join(PKG_SOURCE_DIR, 'db.txt'), encoding="utf8")
src = BeautifulSoup(file.read(), 'lxml')

# List of all genre 'a' tags
aTagList = [i for i in src.find_all('a') if re.match(genrePattern, i['href'])]
aTagList = aTagList[3:]

# List of all Genres and their 'a' tag HREF values
genreList = [i.string for i in aTagList if i.string != None]
genreTags = list(set([i['href'] for i in aTagList]))

# Genre and HREF value dictionary
genres = {i.string: i['href'] for i in aTagList if i.string != None}

# JSON dump files
gL = open(os.path.join(PKG_SOURCE_DIR, 'genreListFile.json'), 'w')
gT = open(os.path.join(PKG_SOURCE_DIR, 'genreTagFile.json'), 'w')
g = open(os.path.join(PKG_SOURCE_DIR, 'genreFile.json'), 'w')

json.dump(genreList, gL)
json.dump(genreTags, gT)
json.dump(genres, g)
