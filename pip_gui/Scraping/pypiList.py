import json
from urllib.request import urlopen

from bs4 import BeautifulSoup

source = urlopen('https://pypi.python.org/simple/').read()
soup = BeautifulSoup(source, 'lxml')

pypi_list = list()

for i in soup.find_all('a'):
    pypi_list.append(i['href'])

file = open('Resource_Files/packageList.json', 'w')
json.dump(pypi_list, file)
