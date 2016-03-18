import os

import SourceModel.SM_File
from SmellDetector import Constants as CONSTS, Utilities


def detectSmells(folder, outputFile):
    detectDeficientEnc(folder, outputFile)

def detectDeficientEnc(folder, outputFile):
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".pp") and not os.path.islink(os.path.join(root, file)):
                fileObj = SourceModel.SM_File.SM_File(os.path.join(root, file))
                detectDefEnc(fileObj, outputFile)

def detectDefEnc(fileObj, outputFile):
    for nodeDecl in fileObj.getNodeDeclarations():
        if nodeDecl.getGlobalVariableCount() > 0:
            Utilities.reportSmell(outputFile, CONSTS.SMELL_DEF_ENC, fileObj.fileName, CONSTS.NODES_RES)
