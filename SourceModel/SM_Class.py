import re
import Utilities
import SourceModel.SM_Constants as SMCONSTS
import SourceModel.SM_Define
import SourceModel.SM_Exec
import SourceModel.SM_FileResource
import SourceModel.SM_PackageResource
import SourceModel.SM_ServiceResource
import SourceModel.SM_CaseStmt
import SourceModel.SM_IfStmt
import SourceModel.SM_User
import SourceModel.SM_Element
import SourceModel.SM_LCOM

class SM_Class(SourceModel.SM_Element.SM_Element):
    def __init__(self, text):
        self.resourceText = text
        self.resourceBodyText = self.extractBodyText(text)
        super().__init__(text)

    def getUsedVariables(self):
        return super().getUsedVariables()

    def extractBodyText(self, text):
        compiledRE = re.compile(SMCONSTS.CLASS_REGEX)
        matches = re.findall(compiledRE, text)
        startIndex = 1
        endIndex = len(text) - 1
        if len(matches)>0:
            startIndex = len(matches[0])
            return text[startIndex:endIndex]
        return text[startIndex:endIndex]

    def getLCOM(self):
        return SourceModel.SM_LCOM.getLCOM(self.resourceBodyText)

    def getBodyTextSize(self):
        loc = self.getLoc()
        return loc, len(self.resourceBodyText)

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