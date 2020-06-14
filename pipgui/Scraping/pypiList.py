import json
import pkg_resources
from urllib.request import urlopen

from bs4 import BeautifulSoup

PACKAGE_DIR = './Resource_Files/Current Packages/'

source = urlopen('https://pypi.python.org/simple/').read()
soup = BeautifulSoup(source, 'lxml')

pypi_list = list()

for i in soup.find_all('a'):
    pypi_list.append(i['href'])

file = open(pkg_resources.resource_filename('pipgui', PACKAGE_DIR + 'packageList.json'), 'w')
json.dump(pypi_list, file)

print("All Packages are updated!!")
