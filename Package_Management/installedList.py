from commands import getoutput
import json

packages = getoutput('pip freeze')
installedPackages = [i.split('==')[0] for i in packages.split('\n')]

print 'Loading installed packages...'
#List of all installed packages
installedPackages = [i for i in installedPackages if ' ' not in i]
print 'Loaded...'
#Dump files
iP = open('Resource_Files/installedPackageList.json', 'w')

json.dump(installedPackages, iP)
