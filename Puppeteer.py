import os
import Analyzer
import Aggregator
import Constants as CONSTS

root = CONSTS.REPO_ROOT
print("Initiating Analyzer...")
for item in os.listdir(root):
    currentFolder = os.path.join(root, item)
    if not os.path.isfile(currentFolder):
        Analyzer.analyze(currentFolder, item)
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