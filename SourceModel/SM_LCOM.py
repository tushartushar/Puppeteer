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
import SourceModel.SM_Class

def getLCOM(bodyText):
    elementList = getDeclElementList(bodyText)
    disconnectedElements = 0
    while len(elementList) > 0:
        disconnectedElements += 1
        curElement = elementList.pop()
        variableList = curElement.getUsedVariables()
        i = 0
        while len(elementList) > 0 and i < len(elementList):
            elementToCompare = elementList[i]
            curVariableList = elementToCompare.getUsedVariables()
            if len(Utilities.intersection(curVariableList, variableList)) > 0:
                variableList = Utilities.summation(curVariableList, variableList)
                elementList.pop(i)
            i += 1

    #print("Computing LCOM : disconnected elements - " + str(disconnectedElements))
    if disconnectedElements > 0:
        LCOM = float("{:.2f}".format(1.0/disconnectedElements))
    else:
        LCOM = float(1.0)
    return LCOM

def getDeclElementList(bodyText):
    exElementList = []
    exElementList.extend(getElementList(SMCONSTS.CLASS_REGEX, bodyText))
    exElementList.extend(getElementList(SMCONSTS.SERVICE_REGEX, bodyText))
    exElementList.extend(getElementList(SMCONSTS.CASE_REGEX, bodyText))
    exElementList.extend(getElementList(SMCONSTS.DEFINE_REGEX, bodyText))
    exElementList.extend(getElementList(SMCONSTS.EXEC_REGEX, bodyText))
    exElementList.extend(getElementList(SMCONSTS.FILE_REGEX, bodyText))
    exElementList.extend(getElementList(SMCONSTS.IF_REGEX, bodyText))
    exElementList.extend(getElementList(SMCONSTS.PACKAGE_REGEX, bodyText))
    exElementList.extend(getElementList(SMCONSTS.USER_REGEX, bodyText))
    filteredList = filterOutInnerElements(exElementList)
    return filteredList

def getElementList(regex, bodyText):
    compiledRE = re.compile(regex)
    exElementList = []
    for match in (compiledRE.findall(bodyText)):
        elementText, startIndex, endIndex = extractElementText(match, bodyText)
        elementObj = getElementObject(elementText, regex)
        exElementList.append(ExElement(elementObj, startIndex, endIndex))

    return exElementList

def extractElementText(initialString, bodyText):
    compiledRE1 = re.compile(r'\{')
    compiledRE2 = re.compile(r'\}')
    curBracketCount = len(compiledRE1.findall(initialString)) - len(compiledRE2.findall(initialString))
    if curBracketCount <= 0:
        return initialString, 0, len(initialString)
    index = bodyText.find(initialString)
    if index < 0:
        return initialString, 0, len(initialString)

    curIndex = index + len(initialString) + 1
    while curBracketCount > 0 and curIndex < len(bodyText):
        if bodyText[curIndex] == '}':
            curBracketCount -= 1
        if bodyText[curIndex] == '{':
            curBracketCount += 1
        curIndex +=1

    return bodyText[index:curIndex], index, curIndex

def getElementObject(elementText, regex):
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
    if regex == SMCONSTS.IF_REGEX:
        return SourceModel.SM_IfStmt.SM_IfStmt(elementText)
    if regex == SMCONSTS.CASE_REGEX:
        return SourceModel.SM_CaseStmt.SM_CaseStmt(elementText)
    if regex == SMCONSTS.USER_REGEX:
        return SourceModel.SM_User.SM_User(elementText)

def sort(exClassElementList):
    result = []
    while len(exClassElementList) > 0:
        largest = findLargest(exClassElementList)
        result.append(largest)
        exClassElementList.remove(largest)
    return result

def findLargest(exClassElementList):
    if len(exClassElementList) > 0:
        largest = exClassElementList[0]
        for item in exClassElementList:
            if (item.endIndex - item.startIndex) > (largest.endIndex - item.startIndex):
                largest = item
        return largest

def filterOutInnerElements(exClassElementList):
    filteredList = []
    exClassElementList = sort(exClassElementList)
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


class ExElement(object):
    def __init__(self, elementObj, startIndex, endIndex):
            self.elementObj = elementObj
            self.startIndex = startIndex
            self.endIndex = endIndex

