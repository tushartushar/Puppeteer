import re

import SourceModel.SM_CaseStmt
import SourceModel.SM_Constants as SMCONSTS
import SourceModel.SM_Define
import SourceModel.SM_Element
import SourceModel.SM_Exec
import SourceModel.SM_File
import SourceModel.SM_FileResource
import SourceModel.SM_IfStmt
import SourceModel.SM_LCOM
import SourceModel.SM_PackageResource
import SourceModel.SM_ServiceResource
import SourceModel.SM_User


class SM_Class(SourceModel.SM_Element.SM_Element):
    def __init__(self, text, name=None):
        self.resourceText = text
        self.className = name
        self.resourceBodyText = self.extractBodyText(text)
        super().__init__(text)

    def getUsedVariables(self):
        return super().getUsedVariables()

    def extractBodyText(self, text):
        compiledRE = re.compile(SMCONSTS.CLASS_REGEX)
        matches = re.findall(compiledRE, text)
        startIndex = 0
        endIndex = len(text) - 1
        if len(matches)>0:
            startIndex = len(matches[0])

        initialString = text[0:startIndex]

        compiledRE1 = re.compile(r'\{')
        compiledRE2 = re.compile(r'\}')
        curBracketCount = len(compiledRE1.findall(initialString)) - len(compiledRE2.findall(initialString))

        curIndex = len(initialString) + 1
        if curBracketCount == 0:
            #This is to find the first "{" since currently there is no { which may happen in case of multi-line class def
            found = False
            while curIndex < len(self.resourceText) and not found:
                if self.resourceText[curIndex] == '{':
                    found = True
                    startIndex = curIndex
                curIndex += 1

        return text[startIndex:endIndex]

    def getLCOM(self):
        fileObj = SourceModel.SM_File.SM_File()
        fileObj.setText(self.resourceBodyText)
        return SourceModel.SM_LCOM.getLCOM(fileObj.getOuterElementList())

    def getBodyTextSize(self):
        loc = self.getLoc()
        return loc, len(self.resourceBodyText)

    def getLocWithoutComments(self):
        totalLines = self.getLoc()
        totalCommentsLines = self.getLinesOfComments()
        return totalLines - totalCommentsLines

    def getLinesOfComments(self):
        counter = self.countEntityDeclaration(SMCONSTS.COMMENT_REGEX, "newLine")
        return counter

    def getLoc(self):
        counter = self.countEntityDeclaration(SMCONSTS.LOC_REGEX, "newLine")
        if counter > 0:
            return counter+1

        if (len(self.resourceBodyText) > 0):
            return 1
        return 0

    def countEntityDeclaration(self, regEx, entityType):
        compiledRE = re.compile(regEx)
        return len(compiledRE.findall(self.resourceBodyText))

    def getClassHierarchyInfo(self):
        match = re.search(SMCONSTS.CLASS_GROUP_REGEX, self.resourceText)
        clsName = ""
        pClsName = ""
        if match:
            clsName = match.group(1)

        match = re.search(SMCONSTS.CLASS_INH_REGEX, self.resourceText)
        if match:
            pClsName = match.group(1)
            #print(clsName + " inherits " + pClsName)
        return clsName, pClsName

    def getResourceName(self):
        match = re.search(SMCONSTS.CLASS_GROUP_REGEX, self.resourceText)
        name =""
        if match:
            name = match.group(1)
        return str(name)

    def getDependentResource(self):
        resultList = []
        self.getDependentResource_(resultList, SMCONSTS.DEPENDENT_PACKAGE, SMCONSTS.DEPENDENT_GROUP_PACKAGE, SMCONSTS.PACKAGE)
        self.getDependentResource_(resultList, SMCONSTS.DEPENDENT_SERVICE, SMCONSTS.DEPENDENT_GROUP_SERVICE, SMCONSTS.SERVICE)
        self.getDependentResource_(resultList, SMCONSTS.DEPENDENT_FILE, SMCONSTS.DEPENDENT_GROUP_FILE, SMCONSTS.FILE)
        self.getDependentResource_(resultList, SMCONSTS.DEPENDENT_CLASS, SMCONSTS.DEPENDENT_GROUP_CLASS, SMCONSTS.CLASS)

        return resultList

    def getDependentResource_(self, resultList, regex, groupRegex, entity):
        compiledRE = re.compile(regex)
        for depItem in compiledRE.findall(self.resourceText):
            match = re.search(groupRegex, depItem)
            if match:
                name = match.group(1)
                if name.startswith(":"):
                    clsName, pClasName = self.getClassHierarchyInfo()
                    if pClasName:
                        name = pClasName + name
                resultList.append((name, entity))
