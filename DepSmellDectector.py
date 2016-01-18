import Utilities
import os
import SourceModel.SM_File
import Constants as CONSTS
import FileOperations

def detectSmells(folder, outputFile):
    detectMissingDep(folder, outputFile)

def detectMissingDep(folder, outputFile):
    detectMissingModules(folder, outputFile)

def detectMissingModules(folder, output):
    abspath, dirs, files = os.walk(folder)
    availableModules = []
    if 'modules' in dirs:
        xpath, availableModules, xfiles = os.walk(os.path.join(folder, 'modules'))
    for file in files:
        if file.endswith(".pp"):
            fileObj = SourceModel.SM_File.SM_File(os.path.join(abspath, file))
            detectMissingModulesByInclude(fileObj, outputFile)

def detectMissingModulesByInclude(fileObj, output):
    includeModuleList = fileObj.getIncludeModules()     
