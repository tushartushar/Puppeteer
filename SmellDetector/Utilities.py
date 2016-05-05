from SmellDetector import Constants as CONSTS


def myPrint(msg):
    if(CONSTS.DEBUG_ON):
        print(msg)

def reportSmell(outputFile, fileName, smellName, reason):
    outputFile.write(smellName + " at " + reason + " in file " + fileName + "\n")
    myPrint(smellName + " at " + reason + " in file " + fileName + "\n")

def intersection(list1, list2):
    return list(set(list1) & set(list2))

def summation(list1, list2):
    return list(set(list1) | set(list2))