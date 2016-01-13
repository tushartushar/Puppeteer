import os
import SourceModel.SM_File
import Utilities
import Constants as CONSTS

def detectSmells(folder, outputFile):
    detectMultifacetedAbs(folder, outputFile)
    detectUnnecessaryAbs(folder, outputFile)
    detectImperativeAbs(folder, outputFile)
    detectDuplicateAbs(folder, outputFile)
    detectMissingAbs(folder, outputFile)

def detectMultifacetedAbs(folder, outputFile):
    detectMultifacetedAbsForm1(folder, outputFile)
    detectMultifacetedAbsForm2(folder, outputFile)

def detectUnnecessaryAbs(folder, outputFile):
    detectUnnAbs(folder, outputFile)

def detectImperativeAbs(folder, outputFile):
    pass

def detectDuplicateAbs(folder, outputFile):
    pass

def detectMissingAbs(folder, outputFile):
    pass

def detectMultifacetedAbsForm1(folder, outputFile):
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".pp"):
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
            if file.endswith(".pp"):
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

def detectUnnAbs(folder, outputFile):
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".pp"):
                fileObj = SourceModel.SM_File.SM_File(os.path.join(root, file))
                detectUnnAbsInClasses(fileObj, outputFile)
                detectUnnAbsInDefine(fileObj, outputFile)
                detectUnnAbsInModules(fileObj, outputFile)

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