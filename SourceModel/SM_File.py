import re

import SourceModel.SM_CaseStmt
import SourceModel.SM_Class
import SourceModel.SM_Constants as SMCONSTS
import SourceModel.SM_Define
import SourceModel.SM_Define
import SourceModel.SM_Element
import SourceModel.SM_Exec
import SourceModel.SM_FileResource
import SourceModel.SM_IfStmt
import SourceModel.SM_IncludeResource
import SourceModel.SM_LCOM
import SourceModel.SM_Node
import SourceModel.SM_PackageResource
import SourceModel.SM_ServiceResource
import SourceModel.SM_User
from SmellDetector import Utilities


class SM_File:

    def __init__(self, file=""):
        if file != "":
            curFile = open(file, 'rt', errors='ignore')
            self.fileText = curFile.read()
            self.resourceBodyText = self.fileText
            self.fileName = file
            curFile.close()

    def setText(self, text):
        self.fileText = text

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

    def getLinesOfCodeWithoutComments(self):
        totalLines = self.getLinesOfCode()
        totalCommentsLines = self.getLinesOfComments()
        return totalLines - totalCommentsLines

    def getLinesOfComments(self):
        counter = self.countEntityDeclaration(SMCONSTS.COMMENT_REGEX, "newLine")
        return counter

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
        index = self.fileText.find(initialString)
        if index < 0:
            return initialString

        compiledRE1 = re.compile(r'\{')
        compiledRE2 = re.compile(r'\}')
        curBracketCount = len(compiledRE1.findall(initialString)) - len(compiledRE2.findall(initialString))

        curIndex = index + len(initialString) + 1
        if curBracketCount == 0:
            #This is to find the first "{" since currently there is no { which may happen in case of multi-line def
            found = False
            while curIndex < len(self.fileText) and not found:
                if self.fileText[curIndex] == '{':
                    found = True
                    curBracketCount = 1
                curIndex += 1

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
        compiledClassNameRE = re.compile(SMCONSTS.CLASS_NAME_REGEX)
        classList = []
        for match in compiledRE.findall(self.fileText):
            className = compiledClassNameRE.findall(match)[0]
            #print("Class name: %s" % (className))
            classText = self.extractResourceText(match)
            Utilities.myPrint("Extracted class declaration: " + classText)
            classObj = SourceModel.SM_Class.SM_Class(classText, className)
            classList.append(classObj)
        return classList

    def getDefineDeclarationList(self):
        compiledRE = re.compile(SMCONSTS.DEFINE_REGEX)
        defineList = []
        for match in compiledRE.findall(self.fileText):
            defineText, s, e = self.extractElementText(match)
            Utilities.myPrint("Extracted define declaration: " + defineText)
            defineObj = SourceModel.SM_Define.SM_Define(defineText)
            defineList.append(defineObj)
        return defineList

    def getLCOM(self):
        return SourceModel.SM_LCOM.getLCOM(self.getOuterElementList())

    def getBodyTextSize(self):
        loc = self.getLinesOfCode()
        return loc, len(self.resourceBodyText)

    def getOuterClassList(self):
        outerElementList = self.getOuterElementList()
        classList = []
        for element in outerElementList:
            if type(element) is SourceModel.SM_Class.SM_Class:
                classList.append(element)
        return classList

    def getOuterDefineList(self):
        outerElementList = self.getOuterElementList()
        defineList = []
        for element in outerElementList:
            if type(element) is SourceModel.SM_Define.SM_Define:
                defineList.append(element)
        return defineList
        # exElementList = []
        # exElementList.extend(self.getElementList(SMCONSTS.DEFINE_REGEX))
        # filteredList = self.filterOutInnerElements(exElementList)
        # return filteredList

    def getOuterElementList(self):
        exElementList = []
        exElementList.extend(self.getElementList(SMCONSTS.CLASS_REGEX))
        exElementList.extend(self.getElementList(SMCONSTS.SERVICE_REGEX))
        exElementList.extend(self.getElementList(SMCONSTS.CASE_REGEX))
        exElementList.extend(self.getElementList(SMCONSTS.DEFINE_REGEX))
        exElementList.extend(self.getElementList(SMCONSTS.EXEC_REGEX))
        exElementList.extend(self.getElementList(SMCONSTS.FILE_REGEX))
        exElementList.extend(self.getElementList(SMCONSTS.IF_REGEX))
        exElementList.extend(self.getElementList(SMCONSTS.PACKAGE_REGEX))
        exElementList.extend(self.getElementList(SMCONSTS.USER_REGEX))
        filteredList = self.filterOutInnerElements(exElementList)
        return filteredList

    def getElementList(self, regex):
        compiledRE = re.compile(regex)
        exElementList = []
        for str in (compiledRE.findall(self.fileText)):
            elementText, startIndex, endIndex = self.extractElementText(str)
            elementObj = self.getElementObject(elementText, regex)
            exElementList.append(ExElement(elementObj, startIndex, endIndex))

        return exElementList

# TODO: Handle variables
# Unwrap classes from list
    def getIncludeClasses(self):
        compiledIncludeRE = re.compile(SMCONSTS.DECLARE_INCLUDE_REGEX)
        compiledResourceRE = re.compile(SMCONSTS.DECLARE_RESOURCE_REGEX)
        declareClassList = []
        declareClassName = ""
        for match in (compiledIncludeRE.findall(self.fileText)):
            #print(match)
            declareClassText = match
            cleanInclude = re.sub(r'^\s*include \[?(.+)\]?\s*$', r'\1', declareClassText)
            #print("Clean include: %s" % cleanInclude)
            class_name = r'(?:Class\[)?\'?\:{0,2}([\w\d\:\-_\$]+)\'?\]?'
            classRE = re.compile(class_name)
            if ',' in cleanInclude:
              classes = cleanInclude.split(',')
              for c in classes:
                for m in classRE.findall(c):
                  # Find a variable value in text
                  if m.startswith('$'):
                    #print("Variable: %s" % m)
                    varRE = r'(?:^|\n)\s*\$[\w\d\-_]+\s?=\s?\'?\"?([\w\d\-_]+)\'?\"?\n'
                    compiledVarRE = re.compile(varRE)
                    for v in (compiledVarRE.findall(self.fileText)):
                      #print(v)
                      declareClassName = v
                      Utilities.myPrint("Extracted include class declaration: " + declareClassText)
                      declareResourceObj = SourceModel.SM_IncludeResource.SM_IncludeResource(declareClassText, declareClassName)
                      declareClassList.append(declareResourceObj)
                      break
                      #print("Variable %s value)
                  #print("Extracted class name: %s" % m)
                  else:
                    declareClassName = m
                    Utilities.myPrint("Extracted include class declaration: " + declareClassText)
                    declareResourceObj = SourceModel.SM_IncludeResource.SM_IncludeResource(declareClassText, declareClassName)
                    declareClassList.append(declareResourceObj)
            else:
              for c in classRE.findall(cleanInclude):
                #print("Extracted class name: %s" % c)
                declareClassName = c
            #print("%s" % includeClassText)
                Utilities.myPrint("Extracted include class declaration: " + declareClassText)
                declareResourceObj = SourceModel.SM_IncludeResource.SM_IncludeResource(declareClassText, declareClassName)
                declareClassList.append(declareResourceObj)
        for match in (compiledResourceRE.findall(self.fileText)):
            #print(match)
            declareClassText = match
            declareClassName = declareClassText
            #print("%s" % includeClassText)
            Utilities.myPrint("Extracted resource class declaration: " + declareClassText)
            declareResourceObj = SourceModel.SM_IncludeResource.SM_IncludeResource(declareClassText, declareClassName)
            declareClassList.append(declareResourceObj)
        return declareClassList


    def extractElementText(self, initialString):
        compiledRE1 = re.compile(r'\{')
        compiledRE2 = re.compile(r'\}')
        curBracketCount = len(compiledRE1.findall(initialString)) - len(compiledRE2.findall(initialString))
        index = self.fileText.find(initialString)
        if index < 0:
            return initialString, 0, len(initialString)
        curIndex = index + len(initialString) + 1
        if curBracketCount == 0:
            #And now we need to find the corresponding ')' to avoid any errors where curly brackets are matched
            #in the parameters itself.
            found = False
            while curIndex < len(self.fileText) and not found:
                if self.fileText[curIndex] == ')':
                    found = True
                curIndex +=1

            #This is to find the first "{" since currently there is no { which may happen in case of multi-line class def
            found = False
            while curIndex < len(self.fileText) and not found:
                if self.fileText[curIndex] == '{':
                    found = True
                    curBracketCount = 1
                curIndex += 1

        while curBracketCount > 0 and curIndex < len(self.fileText):
            if self.fileText[curIndex] == '}':
                curBracketCount -= 1
            if self.fileText[curIndex] == '{':
                curBracketCount += 1
            curIndex +=1

        return self.fileText[index:curIndex], index, curIndex

    def getElementObject(self, elementText, regex):
        if regex == SMCONSTS.CLASS_REGEX:
            return SourceModel.SM_Class.SM_Class(elementText)
        if regex == SMCONSTS.DEFINE_REGEX:
            return SourceModel.SM_Define.SM_Define(elementText)
        if regex == SMCONSTS.EXEC_REGEX:
            return SourceModel.SM_Exec.SM_Exec(elementText)
        if regex == SMCONSTS.FILE_REGEX:
            return SourceModel.SM_FileResource.SM_FileResource(elementText)
        if regex == SMCONSTS.PACKAGE_REGEX:
            return SourceModel.SM_PackageResource.SM_PackageResource(elementText)
        if regex == SMCONSTS.SERVICE_REGEX:
            return SourceModel.SM_ServiceResource.SM_ServiceResource(elementText)
        if regex == SMCONSTS.DECLARE_INCLUDE_REGEX or regex == SMCONSTS.DECLARE_RESOURCE_REGEX:
            return SourceModel.SM_IncludeResource.SM_IncludeResource(elementText)
        if regex == SMCONSTS.IF_REGEX:
            return SourceModel.SM_IfStmt.SM_IfStmt(elementText)
        if regex == SMCONSTS.CASE_REGEX:
            return SourceModel.SM_CaseStmt.SM_CaseStmt(elementText)
        if regex == SMCONSTS.USER_REGEX:
            return SourceModel.SM_User.SM_User(elementText)

    def sort(self, exClassElementList):
        result = []
        while len(exClassElementList) > 0:
            largest = self.findLargest(exClassElementList)
            result.append(largest)
            exClassElementList.remove(largest)
        return result

    def findLargest(self, exClassElementList):
        if len(exClassElementList) > 0:
            largest = exClassElementList[0]
            for item in exClassElementList:
                if (item.endIndex - item.startIndex) > (largest.endIndex - item.startIndex):
                    largest = item
            return largest

    def filterOutInnerElements(self, exClassElementList):
        filteredList = []
        exClassElementList = self.sort(exClassElementList)
        for element in exClassElementList:
            found = False
            for filteredItem in filteredList:
                if element.startIndex >= filteredItem.startIndex and element.endIndex <= filteredItem.endIndex:
                    found = True
                    break
            if found == False:
                filteredList.append(element)
        classElementList = []
        for item in filteredList:
            classElementList.append(item.elementObj)
        return classElementList

    def getMaxNestingDepth(self):
        maxNestingDepth = 0
        curIndex = 0
        curBracketCount = 0
        while curIndex < len(self.fileText):
            if self.fileText[curIndex] == '}':
                curBracketCount -= 1
            if self.fileText[curIndex] == '{':
                curBracketCount += 1
                if curBracketCount > maxNestingDepth:
                    maxNestingDepth = curBracketCount
            curIndex +=1

        return maxNestingDepth

    def getHardCodedStatments(self):
        compiledRE = re.compile(SMCONSTS.HARDCODED_VALUE_REGEX)
        hardCodedStmtList = compiledRE.findall(self.fileText)
        filteredList = []
        for item in hardCodedStmtList:
            #print(item)
            if not (item.__contains__("$") or item.__contains__("Package") or item.__contains__("Service") \
                    or item.__contains__("File")):
                filteredList.append(item)
        #print(filteredList)
        return filteredList

    def getClassHierarchyInfo(self):
        classDecls = self.getClassDeclarationList()
        classList = []
        parentClassList = []
        for aClass in classDecls:
            classes, pClasses = aClass.getClassHierarchyInfo()
            if len(classes) > 0:
                classList.append(classes)
            if len(pClasses) > 0:
                parentClassList.append(pClasses)
        return classList, parentClassList

    def getNodeDeclarations(self):
        compiledRE = re.compile(SMCONSTS.NODE_REGEX)
        nodeResourceList = []
        for match in (compiledRE.findall(self.fileText)):
            nodeResourceText = self.extractResourceText(match)
            Utilities.myPrint("Extracted node declaration: " + nodeResourceText)
            nodeResourceObj = SourceModel.SM_Node.SM_Node(nodeResourceText)
            nodeResourceList.append(nodeResourceObj)
        return nodeResourceList

class ExElement(object):
    def __init__(self, elementObj, startIndex, endIndex):
            self.elementObj = elementObj
            self.startIndex = startIndex
            self.endIndex = endIndex
