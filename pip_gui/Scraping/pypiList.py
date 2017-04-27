from urllib import urlopen
import json
from bs4 import BeautifulSoup

source = urlopen('https://pypi.python.org/simple/').read()
soup = BeautifulSoup(source, 'lxml')

l = list()

for i in soup.find_all('a'):
    l.append(i['href'])

file = open('Resource_Files/packageList.json', 'w')
json.dump(l, file)
