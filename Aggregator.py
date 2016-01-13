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
    multiAbsSmell = 0
    with open(folder + "/" + CONSTS.PUPPETEER_OUT_FILE, 'rt', errors='ignore') as curFile:
        for line in curFile:
            fileCountIndex = line.find(CONSTS.PUPPET_FILE_COUNT)
            if fileCountIndex >= 0:
                fileCount = int(line[fileCountIndex + len(CONSTS.PUPPET_FILE_COUNT):len(line)])

            classCountIndex = line.find(CONSTS.TOTAL_CLASS_DECLS)
            if classCountIndex >= 0:
                classCount = int(line[classCountIndex + len(CONSTS.TOTAL_CLASS_DECLS): len(line)])

            defineCountIndex = line.find(CONSTS.TOTAL_DEFINE_DECLS)
            if defineCountIndex >= 0:
                defineCount = int(line[defineCountIndex + len(CONSTS.TOTAL_DEFINE_DECLS): len(line)])

            fileResourceCountIndex = line.find(CONSTS.TOTAL_FILE_RES_DECLS)
            if fileResourceCountIndex >= 0:
                fileResourceCount = int(line[fileResourceCountIndex + len(CONSTS.TOTAL_FILE_RES_DECLS): len(line)])

            pkgResourceCountIndex = line.find(CONSTS.TOTAL_PACKAGE_RES_DECLS)
            if pkgResourceCountIndex >= 0:
                packageCount = int(line[pkgResourceCountIndex + len(CONSTS.TOTAL_PACKAGE_RES_DECLS): len(line)])

            serviceResourceCountIndex = line.find(CONSTS.TOTAL_SERVICE_RES_DECLS)
            if serviceResourceCountIndex >= 0:
                serviceCount = int(line[serviceResourceCountIndex + len(CONSTS.TOTAL_SERVICE_RES_DECLS): len(line)])

            execCountIndex = line.find(CONSTS.TOTAL_EXEC_DECLS)
            if execCountIndex >= 0:
                execCount = int(line[execCountIndex + len(CONSTS.TOTAL_EXEC_DECLS): len(line)])

            LOCCountIndex = line.find(CONSTS.TOTAL_LOC)
            if LOCCountIndex >= 0:
                LOCCount = int(line[LOCCountIndex + len(CONSTS.TOTAL_LOC): len(line)])

            multiAbsSmellIndex = line.find(CONSTS.SMELL_MUL_ABS_1)
            if multiAbsSmellIndex >= 0:
                multiAbsSmell += 1
            multiAbsSmellIndex2 = line.find(CONSTS.SMELL_MUL_ABS_2)
            if multiAbsSmellIndex2 >= 0:
                multiAbsSmell += 1

    outFile.write(name + "," + str(fileCount) + "," + str(classCount) + "," + str(defineCount) + "," + str(fileResourceCount) +
                  "," + str(packageCount) + "," + str(serviceCount) + "," + str(execCount) + "," + str(LOCCount) + "," +
                  str(multiAbsSmell))
    outFile.write("\n")
