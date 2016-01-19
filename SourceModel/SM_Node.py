import SourceModel.SM_Element
import re
import SourceModel.SM_Constants as SMCONSTS

class SM_Node(SourceModel.SM_Element.SM_Element):
    def __init__(self, text):
        self.resourceText = text
        super().__init__(text)

    def getGlobalVariableCount(self):
        compiledRE = re.compile(SMCONSTS.GLOBAL_VAR_REGEX)
        return len(compiledRE.findall(self.resourceText))