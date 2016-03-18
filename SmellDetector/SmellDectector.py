from SmellDetector import AbsSmellDectector, ModSmellDectector, HieSmellDectector, DepSmellDectector, EncSmellDectector


def detectSmells(folder, outputFile):
    AbsSmellDectector.detectSmells(folder, outputFile)
    EncSmellDectector.detectSmells(folder, outputFile)
    ModSmellDectector.detectSmells(folder, outputFile)
    DepSmellDectector.detectSmells(folder, outputFile)
    HieSmellDectector.detectSmells(folder, outputFile)
