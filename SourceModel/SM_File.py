import re
import Utilities
import SourceModel.SM_FileResource
import SourceModel.SM_ServiceResource
import SourceModel.SM_PackageResource
import SourceModel.SM_Constants as SMCONSTS
import SourceModel.SM_Class
import SourceModel.SM_LCOM
import SourceModel.SM_Define

class SM_File:

    def __init__(self, file):
        curFile = open(file, 'rt', errors='ignore')
        self.fileText = curFile.read()
        self.resourceBodyText = self.fileText
        self.fileName = file
        curFile.close()

    def getNoOfClassDeclarations(self):
        return self.countEntityDeclaration(SMCONSTS.CLASS_REGEX, "class")

    def getNoOfDefineDeclarations(self):
        return self.countEntityDeclaration(SMCONSTS.DEFINE_REGEX, "define")

    def getNoOfFileDeclarations(self):
        return self.countEntityDeclaration(SMCONSTS.FILE_REGEX, "file")

    def getNoOfPackageDeclarations(self):
        return self.countEntityDeclaration(SMCONSTS.PACKAGE_REGEX, "package")

    def getNoOfServiceDeclarations(self):
        return self.countEntityDeclaration(SMCONSTS.SERVICE_REGEX, "service")

    def getNoOfExecDeclarations(self):
        return self.countEntityDeclaration(SMCONSTS.EXEC_REGEX, "exec")

    def getLinesOfCode(self):
        counter = self.countEntityDeclaration(SMCONSTS.LOC_REGEX, "newLine")
        if counter > 0:
            return counter+1

        if (len(self.fileText) > 0):
            return 1
        return 0

    def countEntityDeclaration(self, regEx, entityType):
        compiledRE = re.compile(regEx)
        Utilities.myPrint("Identified " + entityType + " declarations: " + str(compiledRE.findall(self.fileText)) + \
                          " Size: " + str(len(compiledRE.findall(self.fileText))))
        return len(compiledRE.findall(self.fileText))

    def getFileResourceList(self):
        compiledRE = re.compile(SMCONSTS.FILE_REGEX)
        fileResourceList = []
        for match in (compiledRE.findall(self.fileText)):
            fileResourceText = self.extractResourceText(match)
            Utilities.myPrint("Extracted file declaration: " + fileResourceText)
            fileResourceObj = SourceModel.SM_FileResource.SM_FileResource(fileResourceText)
            fileResourceList.append(fileResourceObj)
        return fileResourceList

    def extractResourceText(self, initialString):
        compiledRE1 = re.compile(r'\{')
        compiledRE2 = re.compile(r'\}')
        curBracketCount = len(compiledRE1.findall(initialString)) - len(compiledRE2.findall(initialString))
        if curBracketCount <= 0:
            return initialString
        index = self.fileText.find(initialString)
        if index < 0:
            return initialString

        curIndex = index + len(initialString) + 1
        while curBracketCount > 0 and curIndex < len(self.fileText):
            if self.fileText[curIndex] == '}':
                curBracketCount -= 1
            if self.fileText[curIndex] == '{':
                curBracketCount += 1
            curIndex +=1

        return self.fileText[index:curIndex]

    def getServiceResourceList(self):
        compiledRE = re.compile(SMCONSTS.SERVICE_REGEX)
        serviceResourceList = []
        for match in (compiledRE.findall(self.fileText)):
            serviceResourceText = self.extractResourceText(match)
            Utilities.myPrint("Extracted service declaration: " + serviceResourceText)
            serviceResourceObj = SourceModel.SM_ServiceResource.SM_ServiceResource(serviceResourceText)
            serviceResourceList.append(serviceResourceObj)
        return serviceResourceList

    def getPackageResourceList(self):
        compiledRE = re.compile(SMCONSTS.PACKAGE_REGEX)
        packageResourceList = []
        for match in (compiledRE.findall(self.fileText)):
            packageResourceText = self.extractResourceText(match)
            Utilities.myPrint("Extracted package declaration: " + packageResourceText)
            packageResourceObj = SourceModel.SM_PackageResource.SM_PackageResource(packageResourceText)
            packageResourceList.append(packageResourceObj)
        return packageResourceList

    def getClassDeclarationList(self):
        compiledRE = re.compile(SMCONSTS.CLASS_REGEX)
        classList = []
        for match in compiledRE.findall(self.fileText):
            classText = self.extractResourceText(match)
            Utilities.myPrint("Extracted class declaration: " + classText)
            classObj = SourceModel.SM_Class.SM_Class(classText)
            classList.append(classObj)
        return classList

    def getDefineDeclarationList(self):
        compiledRE = re.compile(SMCONSTS.DEFINE_REGEX)
        defineList = []
        for match in compiledRE.findall(self.fileText):
            defineText = self.extractResourceText(match)
            Utilities.myPrint("Extracted define declaration: " + defineText)
            defineObj = SourceModel.SM_Define.SM_Define(defineText)
            defineList.append(defineObj)
        return defineList

    def getLCOM(self):
        return SourceModel.SM_LCOM.getLCOM(self.resourceBodyText)