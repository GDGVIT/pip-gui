from commands import getoutput
import json

print 'Loading outdated Packages...'
outPackages = getoutput('pip list -o --format=legacy')
outdatedPackages = [i.split(' ')[0] for i in outPackages.split('\n')]

while 'Retrying' in outdatedPackages:
    outdatedPackages.remove('Retrying')
print 'Loaded...'

oP = open('Resource_Files/outdatedPackageList.json', 'w')

json.dump(outdatedPackages, oP)
