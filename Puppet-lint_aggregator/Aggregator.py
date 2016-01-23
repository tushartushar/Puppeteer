import PLConstants as CONSTS
import os

def aggregate(folder, repoName, outFile):
    rule1_count =0
    rule2_count =0
    rule3_count =0
    rule4_count =0
    rule5_count =0
    rule6_count =0
    rule7_count =0
    rule8_count =0
    rule9_count =0
    rule10_count =0
    rule11_count =0
    rule12_count =0
    rule13_count =0


    file = getPuppetLintFile(folder)
    if file:
        with open(os.path.join(folder, file), 'rt', errors='ignore') as curFile:
            for line in curFile:
                rule1_count = getrule1_count( rule1_count, line)
                rule2_count = getrule2_count(rule2_count, line)
                rule3_count = getrule3_count(rule3_count, line)
                rule4_count = getrule4_count(rule4_count, line)
                rule5_count = getrule5_count(rule5_count, line)
                rule6_count = getrule6_count(rule6_count, line)
                rule7_count = getrule7_count(rule7_count, line)
                rule8_count = getrule8_count(rule8_count, line)
                rule9_count = getrule9_count(rule9_count, line)
                rule10_count = getrule10_count(rule10_count, line)
                rule11_count = getrule11_count(rule11_count, line)
                rule12_count = getrule12_count(rule12_count, line)
                rule13_count = getrule13_count(rule13_count, line)


    outFile.write(repoName + "," + str(rule1_count) + "," + str(rule2_count) + "," + str(rule3_count) \
                  + "," + str(rule4_count) + "," + str(rule5_count) + "," + str(rule6_count) + "," + str(rule7_count)\
                  + "," + str(rule8_count) + "," + str(rule9_count) + "," + str(rule10_count) + "," + str(rule11_count)\
                  + "," + str(rule12_count) + "," + str(rule13_count))
    outFile.write("\n")

def getPuppetLintFile(folder):
    for aFile in os.listdir(folder):
        if aFile.endswith(CONSTS.PUPPETLINT_OUT_FILE ):
            return aFile
    return ""

def getrule1_count(count, line):
    index = line.find(CONSTS.RULE1_1)
    if index >= 0:
        count += 1
    return count

def getrule2_count(count, line):
    index = line.find(CONSTS.RULE2_1)
    if index >= 0:
        count += 1

    index = line.find(CONSTS.RULE2_2)
    if index >= 0:
        count += 1
    return count

def getrule3_count(count, line):
    index = line.find(CONSTS.RULE3_1)
    if index >= 0:
        count += 1
    return count

def getrule4_count(count, line):
    index = line.find(CONSTS.RULE4_1)
    if index >= 0:
        count += 1
    return count

def getrule5_count(count, line):
    index = line.find(CONSTS.RULE5_1)
    if index >= 0:
        count += 1
    index = line.find(CONSTS.RULE5_2)
    if index >= 0:
        count += 1
    return count

def getrule6_count(count, line):
    index = line.find(CONSTS.RULE6_1)
    if index >= 0:
        count += 1
    index = line.find(CONSTS.RULE6_2)
    if index >= 0:
        count += 1
    index = line.find(CONSTS.RULE6_3)
    if index >= 0:
        count += 1
    index = line.find(CONSTS.RULE6_4)
    if index >= 0:
        count += 1
    return count

def getrule7_count(count, line):
    index = line.find(CONSTS.RULE7_1)
    if index >= 0:
        count += 1
    index = line.find(CONSTS.RULE7_2)
    if index >= 0:
        count += 1
    index = line.find(CONSTS.RULE7_3)
    if index >= 0:
        count += 1
    return count

def getrule8_count(count, line):
    index = line.find(CONSTS.RULE8_1)
    if index >= 0:
        count += 1
    return count

def getrule9_count(count, line):
    index = line.find(CONSTS.RULE9_1)
    if index >= 0:
        count += 1
    return count

def getrule10_count(count, line):
    index = line.find(CONSTS.RULE10_1)
    if index >= 0:
        count += 1
    index = line.find(CONSTS.RULE10_2)
    if index >= 0:
        count += 1
    index = line.find(CONSTS.RULE10_3)
    if index >= 0:
        count += 1
    index = line.find(CONSTS.RULE10_4)
    if index >= 0:
        count += 1
    index = line.find(CONSTS.RULE10_5)
    if index >= 0:
        count += 1
    index = line.find(CONSTS.RULE10_6)
    if index >= 0:
        count += 1
    return count

def getrule11_count(count, line):
    index = line.find(CONSTS.RULE11_1)
    if index >= 0:
        count += 1
    return count

def getrule12_count(count, line):
    index = line.find(CONSTS.RULE12_1)
    if index >= 0:
        count += 1
    return count

def getrule13_count(count, line):
    index = line.find(CONSTS.RULE13_1)
    if index >= 0:
        count += 1
    return count

