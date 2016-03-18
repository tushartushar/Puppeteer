from SmellDetector import Constants as CONSTS


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
    insModSmellCount = 0
    unsModSmellCount = 0
    tcModSmellCount = 0
    dupAbsSmellCount = 0
    misDepSmellCount = 0
    broHieSmellCount = 0
    haiStrSmellCount = 0
    defEncSmellCount = 0
    weaModSmellCount = 0
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
            insModSmellCount = getInsModSmellCount(insModSmellCount, line)
            unsModSmellCount = getUnsModSmellCount(unsModSmellCount, line)
            tcModSmellCount = getTCModSmellCount(tcModSmellCount, line)
            dupAbsSmellCount = getDupAbsSmellCount(dupAbsSmellCount, line)
            misDepSmellCount = getMisDepSmellCount(misDepSmellCount, line)
            broHieSmellCount = getBroHieSmellCount(broHieSmellCount, line)
            haiStrSmellCount = getHaiStrSmellCount(haiStrSmellCount, line)
            defEncSmellCount = getDefEncSmellCount(defEncSmellCount, line)
            weaModSmellCount = getWeaModSmellCount(weaModSmellCount, line)

    outFile.write(name + "," + str(fileCount) + "," + str(classCount) + "," + str(defineCount) + "," + str(fileResourceCount) +
                  "," + str(packageCount) + "," + str(serviceCount) + "," + str(execCount) + "," + str(LOCCount) + "," +
                  str(multiAbsSmellCount) + "," + str(unnAbsSmellCount) + "," + str(impAbsSmellCount) + "," +
                  str(misAbsSmellCount) + "," + str(insModSmellCount) + "," + str(unsModSmellCount) + "," +
                  str(tcModSmellCount) + "," + str(dupAbsSmellCount) + "," + str(misDepSmellCount) + ',' + str(broHieSmellCount) + "," +
                  str(haiStrSmellCount) + "," + str(defEncSmellCount) + "," + str(weaModSmellCount))

    outFile.write("\n")

def getWeaModSmellCount(weaModSmellCount, line):
    weaModSmellIndex = line.find(CONSTS.SMELL_WEA_MOD)
    if weaModSmellIndex >= 0:
        weaModSmellCount += 1
    return weaModSmellCount

def getDefEncSmellCount(defEncSmellCount, line):
    defEndSmellIndex = line.find(CONSTS.SMELL_DEF_ENC)
    if defEndSmellIndex >= 0:
        defEncSmellCount += 1
    return defEncSmellCount

def getHaiStrSmellCount(haiStrSmellCount, line):
    haiStrSmellIndex = line.find(CONSTS.SMELL_HAI_STR)
    if haiStrSmellIndex >= 0:
        haiStrSmellCount += 1
    return haiStrSmellCount

def getBroHieSmellCount(broHieSmellCount, line):
    broHieSmellIndex = line.find(CONSTS.SMELL_BRO_HIE)
    if broHieSmellIndex >= 0:
        broHieSmellCount += 1
    return broHieSmellCount

def getMisDepSmellCount(misDepSmellCount, line):
    misDepSmellIndex = line.find(CONSTS.SMELL_MIS_DEP)
    if misDepSmellIndex >= 0:
        misDepSmellCount += 1
    return misDepSmellCount

def getDupAbsSmellCount(dupAbsSmellCount, line):
    dupAbsSmellIndex = line.find((CONSTS.SMELL_DUP_ABS))
    if dupAbsSmellIndex >= 0:
        dupAbsSmellCount += 1
    return dupAbsSmellCount

def getTCModSmellCount(tcModSmellCount, line):
    tcModSmellIndex = line.find((CONSTS.SMELL_TC_MOD))
    if tcModSmellIndex >= 0:
        tcModSmellCount += 1
    return tcModSmellCount

def getUnsModSmellCount(unsModSmellCount, line):
    unsModSmellIndex = line.find(CONSTS.SMELL_UNS_MOD_1)
    if unsModSmellIndex >= 0:
        unsModSmellCount +=1

    unsModSmellIndex = line.find(CONSTS.SMELL_UNS_MOD_2)
    if unsModSmellIndex >= 0:
        unsModSmellCount +=1

    unsModSmellIndex = line.find(CONSTS.SMELL_UNS_MOD_3)
    if unsModSmellIndex >= 0:
        unsModSmellCount +=1
    return unsModSmellCount

def getInsModSmellCount(insModSmellCount, line):
    insModSmellIndex = line.find(CONSTS.SMELL_INS_MOD_1)
    if insModSmellIndex >= 0:
        insModSmellCount += 1

    insModSmellIndex = line.find(CONSTS.SMELL_INS_MOD_2)
    if insModSmellIndex >= 0:
        insModSmellCount += 1

    insModSmellIndex = line.find(CONSTS.SMELL_INS_MOD_3)
    if insModSmellIndex >= 0:
        insModSmellCount += 1
    return  insModSmellCount

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
