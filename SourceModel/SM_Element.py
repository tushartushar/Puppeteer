import re
import SourceModel.SM_Constants as SMCONSTS

class SM_Element:
    def __init__(self, text):
        self.resourceText = text

    def getUsedVariables(self):
        compiledRE = re.compile(SMCONSTS.VAR1_REGEX)
        varList = []
        varList.extend(self.extrasStripVar1(compiledRE.findall(self.resourceText)))
        compiledRE = re.compile(SMCONSTS.VAR2_REGEX)
        varList.extend(self.extrasStripVar2(compiledRE.findall(self.resourceText)))
        compiledRE = re.compile(SMCONSTS.VAR3_REGEX)
        varList.extend(self.extrasStripVar3(compiledRE.findall(self.resourceText)))
        compiledRE = re.compile(SMCONSTS.VAR4_REGEX)
        varList.extend(self.extrasStripVar4(compiledRE.findall(self.resourceText)))

        return varList

    def extrasStripVar1(self, matchList):
        return self.extraStrip(matchList, SMCONSTS.VAR1_EX_REGEX)

    def extrasStripVar2(self, matchList):
        return self.extraStrip(matchList, SMCONSTS.VAR2_EX_REGEX)

    def extrasStripVar3(self, matchList):
        return self.extraStrip(matchList, SMCONSTS.VAR3_EX_REGEX)

    def extrasStripVar4(self, matchList):
        return self.extraStrip(matchList, SMCONSTS.VAR4_EX_REGEX)

    def extraStrip(self, matchList, regex):
        varList = []
        for match in matchList:
            m = re.search(regex, match)
            if m:
                if(m.group(1) != ':') or (m.group(1) != '::'):
                    varList.append(m.group(1).strip())

        return varList

    def getLOC(self):
        counter = self.countEntityDeclaration(SMCONSTS.LOC_REGEX, "newLine")
        if counter > 0:
            return counter+1

        if (len(self.resourceText) > 0):
            return 1
        return 0

    def countEntityDeclaration(self, regEx, entityType):
        compiledRE = re.compile(regEx)
        return len(compiledRE.findall(self.resourceText))