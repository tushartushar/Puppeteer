import re

import SourceModel.SM_Constants as SMCONSTS
import SourceModel.SM_Element
from SmellDetector import Utilities


class SM_FileResource(SourceModel.SM_Element.SM_Element):
    def __init__(self, text):
        self.resourceText = text
        super().__init__(text)

    def getUsedVariables(self):
        return super().getUsedVariables()

    def getPhysicalResourceDeclarationCount(self):
        compiledRE = re.compile(r'\'.+\'\W*:|\".+\":')
        tempVar = compiledRE.findall(self.resourceText)
        Utilities.myPrint("Found file declarations: " + str(tempVar))
        return len(tempVar)

    def getResourceName(self):
        match = re.search(SMCONSTS.FILE_GROUP_REGEX, self.resourceText)
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
                resultList.append((name, entity))