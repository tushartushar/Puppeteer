import SourceModel.SM_Element

class SM_Exec(SourceModel.SM_Element.SM_Element):
    def __init__(self, text):
        self.resourceText = text
        super().__init__(text)

    def getUsedVariables(self):
        return super().getUsedVariables()