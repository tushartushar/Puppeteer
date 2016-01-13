import re
import Utilities
import SourceModel.SM_Element

class SM_ServiceResource(SourceModel.SM_Element.SM_Element):
    def __init__(self, text):
        self.resourceText = text
        super().__init__(text)

    def getUsedVariables(self):
        return super().getUsedVariables()

    def getPhysicalResourceDeclarationCount(self):
        compiledRE = re.compile(r'\'.+\'\W*:|\".+\":')
        tempVar = compiledRE.findall(self.resourceText)
        Utilities.myPrint("Found service declarations: " + str(tempVar))
        return len(tempVar)