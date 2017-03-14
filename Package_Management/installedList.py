#Python 2.x

from commands import getoutput
import json

packages = getoutput('pip freeze')
installedPackages = [i.split('==')[0] for i in packages.split('\n')]

#List of all installed packages
installedPackages = [i for i in installedPackages if ' ' not in i]

outPackages = getoutput('pip list -o --format=columns')
outdatedPackages = [i.split(' ')[0] for i in outPackages.split('\n')]

#Dump files
iP = open('/root/Desktop/GDG/PIP_GUI/Resource_Files/installedPackageList.json', 'w')
oP = open('/root/Desktop/GDG/PIP_GUI/Resource_Files/outdatedPackageList.json', 'w')

json.dump(installedPackages, iP)
json.dump(outdatedPackages, oP)
