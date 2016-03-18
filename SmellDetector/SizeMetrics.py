import os

import SourceModel.SM_File
from SmellDetector import Constants as CONSTS, Utilities


def collectSizeMetrics(folder, outputFile):
    totalClasses = 0
    totalDefines = 0
    totalFiles = 0
    totalPackages = 0
    totalServices = 0
    totalExecs = 0
    totalLOC = 0
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".pp") and not os.path.islink(os.path.join(root, file)):
                Utilities.myPrint("Reading file: " + os.path.join(root, file))
                fileObj = SourceModel.SM_File.SM_File(os.path.join(root, file))

                totalClasses += fileObj.getNoOfClassDeclarations()
                totalDefines += fileObj.getNoOfDefineDeclarations()
                totalFiles += fileObj.getNoOfFileDeclarations()
                totalPackages += fileObj.getNoOfPackageDeclarations()
                totalServices += fileObj.getNoOfServiceDeclarations()
                totalExecs += fileObj.getNoOfExecDeclarations()
                totalLOC += fileObj.getLinesOfCode()

    outputFile.write(CONSTS.TOTAL_CLASS_DECLS + str(totalClasses) + "\n")
    Utilities.myPrint(CONSTS.TOTAL_CLASS_DECLS + str(totalClasses))

    outputFile.write(CONSTS.TOTAL_DEFINE_DECLS + str(totalDefines) + "\n")
    Utilities.myPrint(CONSTS.TOTAL_DEFINE_DECLS + str(totalDefines))

    outputFile.write(CONSTS.TOTAL_FILE_RES_DECLS + str(totalFiles) + "\n")
    Utilities.myPrint(CONSTS.TOTAL_FILE_RES_DECLS + str(totalFiles))

    outputFile.write(CONSTS.TOTAL_PACKAGE_RES_DECLS + str(totalPackages) + "\n")
    Utilities.myPrint(CONSTS.TOTAL_PACKAGE_RES_DECLS + str(totalPackages))

    outputFile.write(CONSTS.TOTAL_SERVICE_RES_DECLS + str(totalServices) + "\n")
    Utilities.myPrint(CONSTS.TOTAL_SERVICE_RES_DECLS + str(totalServices))

    outputFile.write(CONSTS.TOTAL_EXEC_DECLS + str(totalExecs) + "\n")
    Utilities.myPrint(CONSTS.TOTAL_EXEC_DECLS + str(totalExecs))

    outputFile.write(CONSTS.TOTAL_LOC + str(totalLOC) + "\n")
    Utilities.myPrint(CONSTS.TOTAL_LOC + str(totalLOC))

