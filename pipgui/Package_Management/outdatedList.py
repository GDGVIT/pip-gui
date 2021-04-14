import os
import json
from subprocess import getoutput


def EasyDir():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(current_dir, r"..\Resource_Files", 'Outdated Packages')


OUTDATED_DIR = EasyDir()

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

oP = open(os.path.join(OUTDATED_DIR, 'outdatedPackageList.json'), 'w')
oP3 = open(os.path.join(OUTDATED_DIR, 'outdatedPackageList3.json'), 'w')

json.dump(outdatedPackages, oP)
json.dump(outdatedPackages3, oP3)
