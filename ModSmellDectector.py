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
    detectInsufficientModForm2(folder, outputFile)
    detectInsufficientModForm3(folder, outputFile)

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

#Form 2 - When the lines of code in a class, define, or a file crosses a certain threshold.
def detectInsufficientModForm2(folder, outputFile):
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".pp"):
                fileObj = SourceModel.SM_File.SM_File(os.path.join(root, file))
                detectInsModForm2(fileObj, outputFile)

def detectInsModForm2(fileObj, outputFile):
    for aClass in fileObj.getOuterClassList():
        if aClass.getLocWithoutComments() > CONSTS.MAX_CLASS_LOC_THRESHOLD:
            Utilities.reportSmell(outputFile, fileObj.fileName, CONSTS.SMELL_INS_MOD_2, CONSTS.CLASS_RES)

    for aDefine in fileObj.getOuterDefineList():
        if aDefine.getLocWithoutComments() > CONSTS.MAX_DEFINE_LOC_THRESHOLD:
            Utilities.reportSmell(outputFile, fileObj.fileName, CONSTS.SMELL_INS_MOD_2, CONSTS.DEFINE_RES)

    if fileObj.getLinesOfCodeWithoutComments() > CONSTS.MAX_MODULE_LOC_THRESHOLD:
            Utilities.reportSmell(outputFile, fileObj.fileName, CONSTS.SMELL_INS_MOD_2, CONSTS.FILE_RES)

#Form 3 - When the complexity (max nesting depth) of a module is greater than a threshold
def detectInsufficientModForm3(folder, outputFile):
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".pp"):
                fileObj = SourceModel.SM_File.SM_File(os.path.join(root, file))
                detectInsModForm3(fileObj, outputFile)

def detectInsModForm3(fileobj, outputFile):
    if fileobj.getMaxNestingDepth() > CONSTS.MAX_NESTING_DEPTH:
        Utilities.reportSmell(outputFile, fileobj.fileName, CONSTS.SMELL_INS_MOD_3, CONSTS.FILE_RES)