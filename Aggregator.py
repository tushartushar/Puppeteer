import Constants as CONSTS

def aggregate(folder, name, outFile):
    fileCount = 0
    classCount = 0
    defineCount = 0
    fileResourceCount = 0
    packageCount = 0
    serviceCount = 0
    execCount = 0
    LOCCount = 0
    multiAbsSmellCount = 0
    unnAbsSmellCount = 0
    impAbsSmellCount = 0
    misAbsSmellCount = 0
    with open(folder + "/" + CONSTS.PUPPETEER_OUT_FILE, 'rt', errors='ignore') as curFile:
        for line in curFile:
            fileCount = getFileCount(fileCount, line)
            classCount = getClassCount(classCount, line)
            defineCount = getDefineCount(defineCount, line)
            fileResourceCount = getFileResourceCount(fileResourceCount, line)
            packageCount = getPackageCount(line, packageCount)
            serviceCount = getServiceCount(line, serviceCount)
            execCount = getExecCount(execCount, line)
            LOCCount = getLOC(LOCCount, line)
            multiAbsSmellCount = getMulAbsSmellCount(line, multiAbsSmellCount)
            unnAbsSmellCount = getUnnAbsSmellCount(line, unnAbsSmellCount)
            impAbsSmellCount = getImpAbsSmellCount(impAbsSmellCount, line)
            misAbsSmellCount = getMisAbsSmellCount(misAbsSmellCount, line)

    outFile.write(name + "," + str(fileCount) + "," + str(classCount) + "," + str(defineCount) + "," + str(fileResourceCount) +
                  "," + str(packageCount) + "," + str(serviceCount) + "," + str(execCount) + "," + str(LOCCount) + "," +
                  str(multiAbsSmellCount) + "," + str(unnAbsSmellCount) + "," + str(impAbsSmellCount) + "," +
                  str(misAbsSmellCount))
    outFile.write("\n")

def getMisAbsSmellCount(misAbsSmellCount, line):
    misAbsSmellIndex = line.find(CONSTS.SMELL_MIS_ABS)
    if misAbsSmellIndex >= 0:
        misAbsSmellCount += 1
    return misAbsSmellCount

def getImpAbsSmellCount(impAbsSmellCount, line):
    impAbsSmellIndex = line.find(CONSTS.SMELL_IMP_ABS)
    if impAbsSmellIndex >= 0:
        impAbsSmellCount += 1
    return impAbsSmellCount


def getUnnAbsSmellCount(line, unnAbsSmellCount):
    unnAbsSmellIndex = line.find(CONSTS.SMELL_UNN_ABS)
    if unnAbsSmellIndex >= 0:
        unnAbsSmellCount += 1
    return unnAbsSmellCount


def getMulAbsSmellCount(line, multiAbsSmellCount):
    multiAbsSmellIndex = line.find(CONSTS.SMELL_MUL_ABS_1)
    if multiAbsSmellIndex >= 0:
        multiAbsSmellCount += 1
    multiAbsSmellIndex2 = line.find(CONSTS.SMELL_MUL_ABS_2)
    if multiAbsSmellIndex2 >= 0:
        multiAbsSmellCount += 1
    return multiAbsSmellCount


def getLOC(LOCCount, line):
    LOCCountIndex = line.find(CONSTS.TOTAL_LOC)
    if LOCCountIndex >= 0:
        LOCCount = int(line[LOCCountIndex + len(CONSTS.TOTAL_LOC): len(line)])
    return LOCCount


def getExecCount(execCount, line):
    execCountIndex = line.find(CONSTS.TOTAL_EXEC_DECLS)
    if execCountIndex >= 0:
        execCount = int(line[execCountIndex + len(CONSTS.TOTAL_EXEC_DECLS): len(line)])
    return execCount


def getServiceCount(line, serviceCount):
    serviceResourceCountIndex = line.find(CONSTS.TOTAL_SERVICE_RES_DECLS)
    if serviceResourceCountIndex >= 0:
        serviceCount = int(line[serviceResourceCountIndex + len(CONSTS.TOTAL_SERVICE_RES_DECLS): len(line)])
    return serviceCount


def getPackageCount(line, packageCount):
    pkgResourceCountIndex = line.find(CONSTS.TOTAL_PACKAGE_RES_DECLS)
    if pkgResourceCountIndex >= 0:
        packageCount = int(line[pkgResourceCountIndex + len(CONSTS.TOTAL_PACKAGE_RES_DECLS): len(line)])
    return packageCount


def getFileResourceCount(fileResourceCount, line):
    fileResourceCountIndex = line.find(CONSTS.TOTAL_FILE_RES_DECLS)
    if fileResourceCountIndex >= 0:
        fileResourceCount = int(line[fileResourceCountIndex + len(CONSTS.TOTAL_FILE_RES_DECLS): len(line)])
    return fileResourceCount


def getDefineCount(defineCount, line):
    defineCountIndex = line.find(CONSTS.TOTAL_DEFINE_DECLS)
    if defineCountIndex >= 0:
        defineCount = int(line[defineCountIndex + len(CONSTS.TOTAL_DEFINE_DECLS): len(line)])
    return defineCount


def getClassCount(classCount, line):
    classCountIndex = line.find(CONSTS.TOTAL_CLASS_DECLS)
    if classCountIndex >= 0:
        classCount = int(line[classCountIndex + len(CONSTS.TOTAL_CLASS_DECLS): len(line)])
    return classCount


def getFileCount(fileCount, line):
    fileCountIndex = line.find(CONSTS.PUPPET_FILE_COUNT)
    if fileCountIndex >= 0:
        fileCount = int(line[fileCountIndex + len(CONSTS.PUPPET_FILE_COUNT):len(line)])
    return fileCount
