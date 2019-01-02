from subprocess import getoutput
import json

print('Loading outdated Packages...')
outPackages = getoutput('pip list -o --format=legacy')
outPackages3 = getoutput('pip3 list -o --format=legacy')

outdatedPackages = [i.split(' ')[0] for i in outPackages.split('\n')]
outdatedPackages3 = [i.split(' ')[0] for i in outPackages3.split('\n')]

while 'Retrying' in outdatedPackages:
    outdatedPackages.remove('Retrying')
while 'Retrying' in outdatedPackages3:
    outdatedPackages3.remove('Retrying')

print('Loaded...')

oP = open('Resource_Files/outdatedPackageList.json', 'w')
oP3 = open('Resource_Files/outdatedPackageList3.json', 'w')

json.dump(outdatedPackages, oP)
json.dump(outdatedPackages3, oP3)
