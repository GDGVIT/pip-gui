from bs4 import BeautifulSoup
import json

#Function to find both occurences of a tag
def indices(string, substring):
    return [string.find(substring), string.find(substring) + string[string.find(substring) + 1:].find(substring)]

#Source Code File
file = open('Resource_Files/db.txt')
src = str(file.read())
file.close()

#List of all Genres and their 'a' tag HREF values
genreList = json.load(open('Resource_Files/genreListFile.json'))
genreTags = json.load(open('Resource_Files/genreTagFile.json'))

#Genre and HREF value dictionary
genres = json.load(open('Resource_Files/genreFile.json'))

#Tag values and their indices
indexDict = {i:max(indices(src, i)) for i in genreTags}

def substr(string, start, tag='ul'):
    sub = string[string[start:].find('<' + tag + '>')+start: string[start:].find('</' + tag + '>') + start + len('</' + tag + '>')]
    aTags = BeautifulSoup(sub, 'html.parser').find_all('a')
    return [i.string for i in aTags]

#Dictionary of genre tags with all relative packages
packageDict = {i:substr(src, indexDict[i]) for i in genreTags}

json.dump(packageDict, open('Resource_Files/packageDictFile.json', 'w'))

k = json.load(open('Resource_Files/packageDictFile.json'))
