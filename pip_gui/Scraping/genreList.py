from bs4 import BeautifulSoup
import re
from pprint import pprint
import json

genrePattern = re.compile(r'#[\w-]+')

#Source Code File
file = open('Resource_Files/db.txt')
src = BeautifulSoup(file.read(), 'lxml')

#List of all genre 'a' tags
aTagList = [i for i in src.find_all('a') if re.match(genrePattern, i['href'])]
aTagList = aTagList[3:]

#List of all Genres and their 'a' tag HREF values
genreList = [i.string for i in aTagList if i.string != None]
genreTags = list(set([i['href'] for i in aTagList]))

#Genre and HREF value dictionary
genres = {i.string:i['href'] for i in aTagList if i.string != None}

#JSON dump files
gL = open('Resource_Files/genreListFile.json', 'w')
gT = open('Resource_Files/genreTagFile.json', 'w')
g = open('Resource_Files/genreFile.json', 'w')

json.dump(genreList, gL)
json.dump(genreTags, gT)
json.dump(genres, g)
