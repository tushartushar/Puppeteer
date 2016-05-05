import os
import re

import SourceModel.SM_File
from SmellDetector import Constants as CONSTS, Utilities


def detectSmells(folder, outputFile):
    detectMultifacetedAbs(folder, outputFile)
    #detectUnnecessaryAbs(folder, outputFile)
    #detectImperativeAbs(folder, outputFile)
    #detectDuplicateAbs(folder, outputFile)
    #detectMissingAbs(folder, outputFile)

def detectMultifacetedAbs(folder, outputFile):
    detectMultifacetedAbsForm1(folder, outputFile)
    detectMultifacetedAbsForm2(folder, outputFile)

def detectUnnecessaryAbs(folder, outputFile):
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".pp") and not os.path.islink(os.path.join(root, file)):
                fileObj = SourceModel.SM_File.SM_File(os.path.join(root, file))
                detectUnnAbsInClasses(fileObj, outputFile)
                detectUnnAbsInDefine(fileObj, outputFile)
                detectUnnAbsInModules(fileObj, outputFile)

def detectImperativeAbs(folder, outputFile):
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".pp") and not os.path.islink(os.path.join(root, file)):
                fileObj = SourceModel.SM_File.SM_File(os.path.join(root, file))
                detectImpAbs(fileObj, outputFile)


def detectImpAbs(fileObj, outputFile):
    execDecls = fileObj.getNoOfExecDeclarations()
    totalDeclarations = fileObj.getNoOfClassDeclarations() + fileObj.getNoOfDefineDeclarations() + \
                        fileObj.getNoOfFileDeclarations() + fileObj.getNoOfPackageDeclarations() + \
                        fileObj.getNoOfServiceDeclarations() + execDecls
    if float(totalDeclarations * CONSTS.IMPABS_THRESHOLD) <= float(
            execDecls) and execDecls > CONSTS.IMPABS_MAXEXECCOUNT:
        Utilities.reportSmell(outputFile, fileObj.fileName, CONSTS.SMELL_IMP_ABS, CONSTS.FILE_RES)

# In order to detect duplicate abstraction smell, we first run cpd on all repositories (repo wise) and the result
# must be stored at the root of each repo in a file ending with "cpd.xml"
def detectDuplicateAbs(folder, outputFile):
    cpdXmlFile = getCpdXmlFile(folder)
    if cpdXmlFile:
        file = open(os.path.join(folder, cpdXmlFile), 'r', errors='ignore')
        fileContent = file.read()
        compiledRE = re.compile("<duplication lines=")
        for i in re.findall(compiledRE, fileContent):
            Utilities.reportSmell(outputFile, folder, CONSTS.SMELL_DUP_ABS, CONSTS.FILE_RES)

def getCpdXmlFile(folder):
    for aFile in os.listdir(folder):
        if aFile == "cpd.xml":
            return aFile
    return ""

def detectMissingAbs(folder, outputFile):
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".pp") and not os.path.islink(os.path.join(root, file)):
                fileObj = SourceModel.SM_File.SM_File(os.path.join(root, file))
                detectMisAbs(fileObj, outputFile)

def detectMisAbs(fileObj, outputFile):
    classAndDefineCount = len(fileObj.getOuterClassList() + fileObj.getOuterDefineList())
    outerElementCount = len(fileObj.getOuterElementList())
    if outerElementCount - classAndDefineCount > CONSTS.MISABS_MAX_NON_ABS_COUNT:
        Utilities.reportSmell(outputFile, fileObj.fileName, CONSTS.SMELL_MIS_ABS, CONSTS.FILE_RES)

def detectMultifacetedAbsForm1(folder, outputFile):
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".pp") and not os.path.islink(os.path.join(root, file)):
                fileObj = SourceModel.SM_File.SM_File(os.path.join(root, file))
                checkWithFileResource(fileObj, outputFile)
                checkWithServiceResource(fileObj, outputFile)
                checkWithPackageResource(fileObj, outputFile)

def checkWithFileResource(fileObj, outputFile):
    fileResourceList = fileObj.getFileResourceList()
    for fileRes in fileResourceList:
        if fileRes.getPhysicalResourceDeclarationCount() > 1:
            Utilities.reportSmell(outputFile, fileObj.fileName, CONSTS.SMELL_MUL_ABS_1, CONSTS.FILE_RES)

def checkWithServiceResource(fileObj, outputFile):
    serviceResourceList = fileObj.getServiceResourceList()
    for serviceRes in serviceResourceList:
        if serviceRes.getPhysicalResourceDeclarationCount() > 1:
            Utilities.reportSmell(outputFile, fileObj.fileName, CONSTS.SMELL_MUL_ABS_1, CONSTS.SERVICE_RES)

def checkWithPackageResource(fileObj, outputFile):
    packageResourceList = fileObj.getPackageResourceList()
    for packageRes in packageResourceList:
        if packageRes.getPhysicalResourceDeclarationCount() > 1:
            Utilities.reportSmell(outputFile, fileObj.fileName, CONSTS.SMELL_MUL_ABS_1, CONSTS.PACKAGE_RES)

# Please note that since we are considering an abstraction as either a class, define, or a module, we are computing
# the LCOM values separately for them. Therefore, it is quite possible that we have multiple 'multifaceted abstraction'
# smell in a single file.
def detectMultifacetedAbsForm2(folder, outputFile):
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".pp") and not os.path.islink(os.path.join(root, file)):
                fileObj = SourceModel.SM_File.SM_File(os.path.join(root, file))
                detectMulAbsInClass(fileObj, outputFile)
                detectMulAbsInDefine(fileObj, outputFile)
                detectMulAbsInModule(fileObj, outputFile)

def detectMulAbsInClass(fileObj, outputFile):
    classList = fileObj.getClassDeclarationList()
    for aClass in classList:
        lcom = aClass.getLCOM()
        if lcom < CONSTS.LCOM_THRESHOLD:
            Utilities.reportSmell(outputFile, fileObj.fileName, CONSTS.SMELL_MUL_ABS_2, CONSTS.CLASS_RES)

def detectMulAbsInDefine(fileObj, outputFile):
    defineList = fileObj.getDefineDeclarationList()
    for aDefine in defineList:
        if aDefine.getLCOM() < CONSTS.LCOM_THRESHOLD:
            Utilities.reportSmell(outputFile, fileObj.fileName, CONSTS.SMELL_MUL_ABS_2, CONSTS.DEFINE_RES)

def detectMulAbsInModule(fileObj, outputFile):
    if fileObj.getLCOM() < CONSTS.LCOM_THRESHOLD:
        Utilities.reportSmell(outputFile, fileObj.fileName, CONSTS.SMELL_MUL_ABS_2, CONSTS.FILE_RES)

def detectUnnAbsInClasses(fileObj, outputFile):
    classList = fileObj.getClassDeclarationList()
    for aClass in classList:
        lineCount, textSizeCount = aClass.getBodyTextSize()
        if lineCount < CONSTS.LOC_THRESHOLD_UNNABS and textSizeCount < CONSTS.SIZE_THRESHOLD_UNNABS:
            Utilities.reportSmell(outputFile, fileObj.fileName, CONSTS.SMELL_UNN_ABS, CONSTS.CLASS_RES)

def detectUnnAbsInDefine(fileObj, outputFile):
    defineList = fileObj.getDefineDeclarationList()
    for aDefine in defineList:
        lineCount, textSizeCount = aDefine.getBodyTextSize()
        if lineCount < CONSTS.LOC_THRESHOLD_UNNABS and textSizeCount < CONSTS.SIZE_THRESHOLD_UNNABS:
            Utilities.reportSmell(outputFile, fileObj.fileName, CONSTS.SMELL_UNN_ABS, CONSTS.DEFINE_RES)

def detectUnnAbsInModules(fileObj, outputFile):
    lineCount, textSizeCount = fileObj.getBodyTextSize()
    if lineCount < CONSTS.LOC_THRESHOLD_UNNABS and textSizeCount < CONSTS.SIZE_THRESHOLD_UNNABS:
        Utilities.reportSmell(outputFile, fileObj.fileName, CONSTS.SMELL_UNN_ABS, CONSTS.DEFINE_RES)
