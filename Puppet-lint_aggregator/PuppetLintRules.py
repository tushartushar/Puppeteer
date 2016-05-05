import os

import PLConstants as CONSTS

import Aggregator
import Analyzer

root = CONSTS.REPO_ROOT
print("Initiating Custom Puppet-Lint Analyzer...")
totalRepos = len(os.listdir(root))
currentItem = 0
for item in os.listdir(root):
    currentFolder = os.path.join(root, item)
    if not os.path.isfile(currentFolder):
        Analyzer.analyze(currentFolder, item)
    currentItem += 1
    print (str("{:.2f}".format(float(currentItem * 100)/float(totalRepos))) + "% analysis done.")
print("Custom Puppet-Lint Analyzer - Done.")

print("Initiating Puppet-Lint aggregator...")
aggregatedFile = open(root + "/" + CONSTS.AGGREGATOR_FILE, 'wt')
aggregatedFile.write(CONSTS.HEADER)
for item in os.listdir(root):
    currentFolder = os.path.join(root, item)
    if not os.path.isfile(currentFolder):
        Aggregator.aggregate(currentFolder, item, aggregatedFile)
aggregatedFile.close()
print("Puppet-Lint aggregator - Done.")
