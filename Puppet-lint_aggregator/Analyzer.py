import PLConstants as CONSTS
import os
import re

def analyze(folder, repoName):
    outputFile = open(folder + "/" + CONSTS.PUPPETLINT_OUT_FILE, 'a')

    identifyIncompleteTasks(folder, outputFile)
    identifyImportUsage(folder, outputFile)
    identifyComplexExpression(folder, outputFile)
    identifyMissingElse(folder, outputFile)

    outputFile.close()
    return

def identifyIncompleteTasks(folder, outputFile):
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".pp") and not os.path.islink(os.path.join(root, file)):
                file_ = open(os.path.join(root, file), 'r', errors='ignore')
                fileText = file_.read()
                compiledRE = re.compile(r'\btodo\b', flags=re.IGNORECASE)
                for match in (compiledRE.findall(fileText)):
                    reportSmell(outputFile, file, CONSTS.SMELLS_INC_TSK, "todo")
                compiledRE = re.compile(r'\bfixme\b', flags=re.IGNORECASE)
                for match in (compiledRE.findall(fileText)):
                    reportSmell(outputFile, os.path.join(root,file), CONSTS.SMELLS_INC_TSK, "fixme")

def identifyImportUsage(folder, outputFile):
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".pp") and not os.path.islink(os.path.join(root, file)):
                file_ = open(os.path.join(root, file), 'r', errors='ignore')
                fileText = file_.read()
                compiledRE = re.compile(r'\bimport\b')
                for match in (compiledRE.findall(fileText)):
                    reportSmell(outputFile, os.path.join(root,file), CONSTS.SMELLS_DEP_STM, "import")

def identifyComplexExpression(folder, outputFile):
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".pp") and not os.path.islink(os.path.join(root, file)):
                detectComplexExpr(os.path.join(root,file), outputFile)


def detectComplexExpr(file, outputFile):
    file_ = open(file, 'r', errors='ignore')
    fileText = file_.read()
    compiledRE = re.compile(r'\bif .+?\{')
    for match in (compiledRE.findall(fileText)):
        if getNoOfOperators(match) > 2:
            reportSmell(outputFile, file, CONSTS.SMELLS_COM_EXP, "complex exp")


def identifyMissingElse(folder, outputFile):
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".pp") and not os.path.islink(os.path.join(root, file)):
                file_ = open(os.path.join(root, file), 'r', errors='ignore')
                fileText = file_.read()
                compiledRE = re.compile(r'\belsif .+?\{')
                for match in (compiledRE.findall(fileText)):
                    index = fileText.find(match) + len(match) + 1
                    brCount = 1
                    while index < len(fileText) and brCount > 0:
                        if fileText[index] == "}":
                            brCount -= 1
                        if fileText[index] == "{":
                            brCount += 1
                        index += 1
                    while index < len(fileText):
                        if fileText[index]==" " or fileText[index]=="\n":
                            index += 1
                        else:
                            if (fileText[index] == "e" and fileText[index+1] == "l" and fileText[index + 2] == "s"
                                    and fileText[index + 3] == "i" and fileText[index+4] == "f"):
                                break
                            else:
                                if not (fileText[index] == "e" and fileText[index+1] == "l" and fileText[index + 2] == "s"
                                        and fileText[index + 3] == "e"):
                                    reportSmell(outputFile, os.path.join(root,file), CONSTS.SMELLS_MIS_ELS, "missing else")
                                    break
                            index += 1

def reportSmell(outputFile, fileName, smellName, reason):
    outputFile.write(smellName + " at " + reason + " in file " + fileName + "\n")

def getNoOfOperators(str):
    count = 0
    compiledRE = re.compile(r' and ')
    count += len(re.findall(compiledRE, str))
    compiledRE = re.compile(r' or ')
    count += len(re.findall(compiledRE, str))
    compiledRE = re.compile(r'!')
    count += len(re.findall(compiledRE, str))

    return count
