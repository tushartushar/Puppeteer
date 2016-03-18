import os

import SourceModel.SM_File
from SmellDetector import Constants as CONSTS, Utilities


def detectSmells(folder, outputFile):
    detectMissingDep(folder, outputFile)

def detectMissingDep(folder, outputFile):
    detectMissingModules(folder, outputFile)

def detectMissingModules(folder, outputFile):
    #print("%s" % (inspect.stack()[0][3]))
    classNamesSet = set()
    includeClassSet = set()
    for abspath, dirs, files in os.walk(folder):
        for file in files:
            #print(file)
            if file.endswith(".pp") and not os.path.islink(os.path.join(abspath, file)):
                #print(file)
                fileObj = SourceModel.SM_File.SM_File(os.path.join(abspath, file))
                classNames, fileIncludes = detectMissingClassesByInclude(fileObj, outputFile)
                #print("Classes: %s" % ','.join(n for n in classNames))
                classNamesSet = classNamesSet.union(classNames)
                #print("Union with %s: %s" % (','.join(n for n in classNames), ','.join(n for n in classNamesSet)))
                includeClassSet = includeClassSet.union(fileIncludes)
    #print("%s: Classes: %s" % (inspect.stack()[0][3], ','.join(n for n in classNamesSet)))
    #print("%s: Class includes: %s" % (inspect.stack()[0][3], ','.join(i for i in includeClassSet)))
    missingDependencySet = includeClassSet.difference(classNamesSet)
    #print(includeClassSet)
    #print(classNamesSet)
    #print(missingDependencySet)
    Utilities.myPrint("Missing dependency set: %s" % ','.join(c for c in missingDependencySet))
    #for md in missingDependencySet:
        #Utilities.reportSmell(outputFile, folder, CONSTS.SMELL_MIS_DEP, CONSTS.FILE_RES)
    with open('missDependencies.puppeteer.txt', 'a+') as f:
        for md in missingDependencySet:
            f.write("%s\n" % md)
            Utilities.reportSmell(outputFile, folder, CONSTS.SMELL_MIS_DEP, CONSTS.FILE_RES)

def detectMissingClassesByInclude(fileObj, outputFile):
    #print("%s" % (inspect.stack()[0][3]))
    classList = fileObj.getClassDeclarationList()
    #print("%s: All names: %s" % (inspect.stack()[0][3], ','.join(c.className for c in classList)))
    classNames = {c.className for c in classList}
    #print("%s: Class names: %s" % (inspect.stack()[0][3], ','.join(n for n in classNames)))
    includeClassList = fileObj.getIncludeClasses()
    includeClassNames = {i.className for i in includeClassList}
    #print("%s: Class include: %s" % (inspect.stack()[0][3], ','.join(i for i in includeClassNames)))
    #exit(1)
    return classNames, includeClassNames
