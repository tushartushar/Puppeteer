import AbsSmellDectector
import EncSmellDectector
import ModSmellDectector
import DepSmellDectector
import HieSmellDectector

def detectSmells(folder, outputFile):
    AbsSmellDectector.detectSmells(folder, outputFile)
    EncSmellDectector.detectSmells(folder, outputFile)
    ModSmellDectector.detectSmells(folder, outputFile)
    DepSmellDectector.detectSmells(folder, outputFile)
    HieSmellDectector.detectSmells(folder, outputFile)
