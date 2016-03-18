import SmellDetector.Constants as CONSTS
from SmellDetector import SmellDectector, SizeMetrics, FileOperations, Utilities


def analyze(folder, repoName):
    outputFile = open(folder + "/" + CONSTS.PUPPETEER_OUT_FILE, 'w')

    puppetFileCount = FileOperations.countPuppetFiles(folder)
    outputFile.write(CONSTS.PUPPET_FILE_COUNT + str(puppetFileCount) + "\n")
    Utilities.myPrint(CONSTS.PUPPET_FILE_COUNT + str(puppetFileCount))

    SizeMetrics.collectSizeMetrics(folder, outputFile)

    SmellDectector.detectSmells(folder, outputFile)

    outputFile.close()
    return