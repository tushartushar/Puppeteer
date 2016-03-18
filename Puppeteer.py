import os

import Aggregator
from SmellDetector import Constants as CONSTS, Analyzer

root = CONSTS.REPO_ROOT
print("Initiating Analyzer...")
totalRepos = len(os.listdir(root))
currentItem = 0
for item in os.listdir(root):
    currentFolder = os.path.join(root, item)
    #print("Anlyzing: " + currentFolder)
    if not os.path.isfile(currentFolder):
        Analyzer.analyze(currentFolder, item)
    currentItem += 1
    print (str("{:.2f}".format(float(currentItem * 100)/float(totalRepos))) + "% analysis done.")
print("Analyzer - Done.")

print("Initiating metrics and smells aggregator...")
aggregatedFile = open(root + "/" + CONSTS.AGGREGATOR_FILE, 'wt')
aggregatedFile.write(CONSTS.CSV_HEADER)
for item in os.listdir(root):
    currentFolder = os.path.join(root, item)
    if not os.path.isfile(currentFolder):
        Aggregator.aggregate(currentFolder, item, aggregatedFile)
aggregatedFile.close()
print("Metrics and smells aggregator - Done.")