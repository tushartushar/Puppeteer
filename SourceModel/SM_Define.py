import SourceModel.SM_Element
import SourceModel.SM_LCOM
import re
import SourceModel.SM_Constants as SMCONSTS

class SM_Define(SourceModel.SM_Element.SM_Element):
    def __init__(self, text):
        self.resourceText = text
        self.resourceBodyText = self.extractBodyText(text)
        super().__init__(text)

    def getUsedVariables(self):
        return super().getUsedVariables()

    def getLCOM(self):
        return SourceModel.SM_LCOM.getLCOM(self.resourceBodyText)

    def extractBodyText(self, text):
        compiledRE = re.compile(SMCONSTS.DEFINE_REGEX)
        matches = re.findall(compiledRE, text)
        startIndex = 1
        endIndex = len(text) - 1
        if len(matches)>0:
            startIndex = len(matches[0])
            return text[startIndex:endIndex]
        return text[startIndex:endIndex]