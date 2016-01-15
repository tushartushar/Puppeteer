import SourceModel.SM_Element
import SourceModel.SM_LCOM
import re
import SourceModel.SM_Constants as SMCONSTS
import SourceModel.SM_File

class SM_Define(SourceModel.SM_Element.SM_Element):
    def __init__(self, text):
        self.resourceText = text
        self.resourceBodyText = self.extractBodyText(text)
        super().__init__(text)

    def getUsedVariables(self):
        return super().getUsedVariables()

    def getLCOM(self):
        fileObj = SourceModel.SM_File.SM_File()
        fileObj.setText(self.resourceBodyText)
        return SourceModel.SM_LCOM.getLCOM(fileObj.getOuterElementList())

    def extractBodyText(self, text):
        compiledRE = re.compile(SMCONSTS.DEFINE_REGEX)
        matches = re.findall(compiledRE, text)
        startIndex = 0
        endIndex = len(text) - 1
        if len(matches)>0:
            #print(matches)
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

    def getLocWithoutComments(self):
        totalLines = self.getLoc()
        totalCommentsLines = self.getLinesOfComments()
        return totalLines - totalCommentsLines

    def getLinesOfComments(self):
        counter = self.countEntityDeclaration(SMCONSTS.COMMENT_REGEX, "newLine")
        return counter

    def countEntityDeclaration(self, regEx, entityType):
        compiledRE = re.compile(regEx)
        return len(compiledRE.findall(self.resourceBodyText))
