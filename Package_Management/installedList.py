#Python 2.x

from commands import getoutput
import json

packages = getoutput('pip freeze')
installedPackages = [i.split('==')[0] for i in packages.split('\n')]

#List of all installed packages
installedPackages = [i for i in installedPackages if ' ' not in i]

print 'Listing outdated packages:'
outPackages = getoutput('pip list -o --format=legacy')
outdatedPackages = [i.split(' ')[0] for i in outPackages.split('\n')]

while 'Retrying' in outdatedPackages:
    outdatedPackages.remove('Retrying')

#Dump files
iP = open('../Resource_Files/installedPackageList.json', 'w')
oP = open('../Resource_Files/outdatedPackageList.json', 'w')

json.dump(installedPackages, iP)
json.dump(outdatedPackages, oP)
