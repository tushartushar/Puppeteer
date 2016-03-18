from SmellDetector import Utilities


def getLCOM(elementList):
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



