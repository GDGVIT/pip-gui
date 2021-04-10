import os
import json
from subprocess import getoutput


def EasyDir():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(current_dir, r"..\Resource_Files", 'Installed Packages')


INSTALLED_DIR = EasyDir()

packages = getoutput('pip freeze')
packages3 = getoutput('pip3 freeze')

installedPackages = [i.split('==')[0] for i in packages.split('\n')]
installedPackages3 = [i.split('==')[0] for i in packages3.split('\n')]

print('Loading installed packages...')
# List of all installed packages
installedPackages = [i for i in installedPackages if ' ' not in i]
installedPackages3 = [i for i in installedPackages3 if ' ' not in i]

print('Loaded...')
# Dump files
iP = open(os.path.join(INSTALLED_DIR, 'installedPackageList.json'), 'w')
iP3 = open(os.path.join(INSTALLED_DIR, 'installedPackageList3.json'), 'w')

json.dump(installedPackages, iP)
json.dump(installedPackages3, iP3)
