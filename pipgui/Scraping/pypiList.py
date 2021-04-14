import os
import json
from urllib.request import urlopen
from bs4 import BeautifulSoup


def EasyDir():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(current_dir, r"..\Resource_Files", 'Current Packages')


PACKAGE_DIR = EasyDir()

source = urlopen('https://pypi.python.org/simple/').read()
soup = BeautifulSoup(source, 'lxml')

pypi_list = list()

for i in soup.find_all('a'):
    pypi_list.append(i['href'])

file = open(os.path.join(PACKAGE_DIR, 'packageList.json'), 'w')
json.dump(pypi_list, file)

print("All Packages are updated!!")
