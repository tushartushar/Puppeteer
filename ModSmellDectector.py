import Utilities
import os
import SourceModel.SM_File
import Constants as CONSTS
import FileOperations

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
    detectUnstructuredModForm1(folder, outputFile)
    detectUnstructuredModForm2(folder, outputFile)
    detectUnstructuredModForm3(folder, outputFile)

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

#Form 1 - size of the upper-level manifests folder when modules folder is absent, or both modules and manifests folder not present
def detectUnstructuredModForm1(folder, outputFile):
    if isModulesExists(folder):
        return
    manifestsFolder = getManifestsFolder(folder) #repo-level manifests folder
    if manifestsFolder == "":
        Utilities.reportSmell(outputFile, manifestsFolder, CONSTS.SMELL_UNS_MOD_1, CONSTS.REPO_MANIFEST)
        return
    if FileOperations.countPuppetFiles(manifestsFolder) > CONSTS.MAX_MANIFESTS_PUPPET_FILES:
        Utilities.reportSmell(outputFile, manifestsFolder, CONSTS.SMELL_UNS_MOD_1, CONSTS.REPO_MANIFEST)

def isModulesExists(folder):
    for aFile in os.listdir(folder):
        if os.path.isdir(os.path.join(folder,aFile)):
            if aFile.__contains__(CONSTS.MODULES):
                return True
    return False

def getModulesFolder(folder):
    for aFile in os.listdir(folder):
        if os.path.isdir(os.path.join(folder,aFile)):
            if aFile.__contains__(CONSTS.MODULES):
                return os.path.join(folder, aFile)
    return ""

def getManifestsFolder(folder):
    for aFile in os.listdir(folder):
        if os.path.isdir(os.path.join(folder,aFile)):
            if aFile == CONSTS.MANIFESTS:
                return os.path.join(folder, aFile)
    return ""

#Form 2 - In each module, manifest folder must be present
def detectUnstructuredModForm2(folder, outputFile):
    modulesFolder = getModulesFolder(folder)
    if modulesFolder:
        for dir in os.listdir(modulesFolder):
            if os.path.isdir(os.path.join(modulesFolder, dir)):
                detectUnsModForm2(os.path.join(modulesFolder, dir), outputFile)

def detectUnsModForm2(folder, outputFile):
    if not getManifestsFolder(folder):
        Utilities.reportSmell(outputFile,folder, CONSTS.SMELL_UNS_MOD_2, CONSTS.MODULE_MANIFEST)

#Form 3 - When a module contains other than recommended folders/files
def detectUnstructuredModForm3(folder, outputFile):
    modulesFolder = getModulesFolder(folder)
    if modulesFolder:
        for dir in os.listdir(modulesFolder):
            detectUnsModForm3(os.path.join(modulesFolder, dir), outputFile)

def detectUnsModForm3(folder, outputFile):
    counter = 0
    if os.path.isdir(folder):
        for dir in os.listdir(folder):
            if not (dir == "files" or dir == "manifests" or dir == "templates" or dir == "lib" or dir == "tests" or
                            dir == "spec" or dir.__contains__("readme") or dir.__contains__("README") or
                        dir.__contains__("license") or dir.__contains__("LICENSE") or dir.__contains__("metadata")):
                counter += 1

    if counter > CONSTS.MAX_ALLOWED_NONSTANDARD_FILES:
        Utilities.reportSmell(outputFile, folder, CONSTS.SMELL_UNS_MOD_3, CONSTS.OTHERFILES)