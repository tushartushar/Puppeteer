import Utilities
import os
import SourceModel.SM_File
import Constants as CONSTS

def detectSmells(folder, outputFile):
    detectInsufficientMod(folder, outputFile)
    detectUnstructuredMod(folder, outputFile)
    detectTightlyCoupledMod(folder, outputFile)
    detectMissingDep(folder, outputFile)

def detectInsufficientMod(folder, outputFile):
    detectInsufficientModForm1(folder, outputFile)

def detectUnstructuredMod(folder, outputFile):
    pass

def detectTightlyCoupledMod(folder, outputFile):
    pass

def detectMissingDep(folder, outputFile):
    pass

#Form 1 - If a file contains declaration of more than one class/define
def detectInsufficientModForm1(folder, outputFile):
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".pp"):
                fileObj = SourceModel.SM_File.SM_File(os.path.join(root, file))
                detectInsModForm1(fileObj, outputFile)


def detectInsModForm1(fileObj, outputFile):
    classDefineDeclCount = len(fileObj.getOuterClassList()) + len(fileObj.getOuterDefineList())
    if classDefineDeclCount > 1:
        Utilities.reportSmell(outputFile, fileObj.fileName, CONSTS.SMELL_INS_MOD_1, CONSTS.FILE_RES)