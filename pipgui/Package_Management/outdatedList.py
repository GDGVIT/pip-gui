import json
import pkg_resources
from subprocess import getoutput

OUTDATED_DIR = './Resource_Files/Outdated Packages/'

print('Loading outdated Packages...')
outPackages = getoutput('pip list -o')
outPackages3 = getoutput('pip3 list -o')

outdatedPackages = [i.split(' ')[0] for i in outPackages.split('\n')[2:]]
outdatedPackages3 = [i.split(' ')[0] for i in outPackages3.split('\n')[2:]]

while 'Retrying' in outdatedPackages:
    outdatedPackages.remove('Retrying')
while 'Retrying' in outdatedPackages3:
    outdatedPackages3.remove('Retrying')

print('Loaded...')

oP = open(pkg_resources.resource_filename('pipgui', OUTDATED_DIR + 'outdatedPackageList.json'), 'w')
oP3 = open(pkg_resources.resource_filename('pipgui', OUTDATED_DIR + 'outdatedPackageList3.json'), 'w')

json.dump(outdatedPackages, oP)
json.dump(outdatedPackages3, oP3)
