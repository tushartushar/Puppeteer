import os

import SourceModel.SM_File
from SmellDetector import Constants as CONSTS, Utilities


def detectSmells(folder, outputFile):
    detectBrokenHie(folder, outputFile)

def detectBrokenHie(folder, outputFile):
    modulesFolder = getModulesFolder(folder)
    if modulesFolder:
        for dir in os.listdir(modulesFolder):
            if os.path.isdir(os.path.join(modulesFolder, dir)):
                detectBroHierarchy(os.path.join(modulesFolder, dir), outputFile)

def detectBroHierarchy(folder, outputFile):
    classNames, superClassNames = collectClassNames(folder)
    #print("classNames: " + str(classNames))
    #print("superClassNames: " + str(superClassNames))
    for superClass in superClassNames:
        if not classNames.__contains__(superClass):
            Utilities.reportSmell(outputFile, folder, CONSTS.SMELL_BRO_HIE, CONSTS.MODULE_RES)

def getModulesFolder(folder):
    for aFile in os.listdir(folder):
        if os.path.isdir(os.path.join(folder,aFile)):
            if aFile.__contains__(CONSTS.MODULES):
                return os.path.join(folder, aFile)
    return ""

def collectClassNames(folder):
    classNames = []
    parentClassNames = []
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".pp") and not os.path.islink(os.path.join(root, file)):
                fileObj = SourceModel.SM_File.SM_File(os.path.join(root, file))
                classes, pClasses = fileObj.getClassHierarchyInfo()
                if len(classes) > 0:
                    classNames.extend(classes)
                if len(pClasses) > 0:
                    parentClassNames.extend(pClasses)
    return classNames, parentClassNames
