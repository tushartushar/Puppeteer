import os

import Graph.GR_Constants as GRCONSTS
import Graph.Graph
import Graph.GraphNode
import Graph.Resource
import SmellDetector.Constants as CONSTS
import SourceModel.SM_File
from SmellDetector import FileOperations, Utilities


def detectSmells(folder, outputFile):
    detectInsufficientMod(folder, outputFile)
    detectUnstructuredMod(folder, outputFile)
    detectTightlyCoupledMod(folder, outputFile)
    detectHairballStrAndWeakendMod(folder, outputFile)


def detectInsufficientMod(folder, outputFile):
    detectInsufficientModForm1(folder, outputFile)
    detectInsufficientModForm2(folder, outputFile)
    detectInsufficientModForm3(folder, outputFile)

def detectUnstructuredMod(folder, outputFile):
    detectUnstructuredModForm1(folder, outputFile)
    detectUnstructuredModForm2(folder, outputFile)
    detectUnstructuredModForm3(folder, outputFile)

def detectTightlyCoupledMod(folder, outputFile):
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".pp") and not os.path.islink(os.path.join(root, file)):
                fileObj = SourceModel.SM_File.SM_File(os.path.join(root, file))
                detectTCMod(fileObj, outputFile)

def detectHairballStrAndWeakendMod(folder, outputFile):
    graph = getGraph(folder)
    detectHaiStr(graph, folder, outputFile) #Excessive avg dependency
    detectWeakendMod(graph, folder, outputFile) #modularity ratio

#Form 1 - If a file contains declaration of more than one class/define
def detectInsufficientModForm1(folder, outputFile):
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".pp") and not os.path.islink(os.path.join(root, file)):
                fileObj = SourceModel.SM_File.SM_File(os.path.join(root, file))
                detectInsModForm1(fileObj, outputFile)


def detectInsModForm1(fileObj, outputFile):
    classDefineDeclCount = len(fileObj.getOuterClassList()) + len(fileObj.getOuterDefineList())
    if classDefineDeclCount > 1:
        Utilities.reportSmell(outputFile, fileObj.fileName, CONSTS.SMELL_INS_MOD_1, CONSTS.FILE_RES)

#Form 2 - When the lines of code in a class, define, or a file crosses a certain threshold.
def detectInsufficientModForm2(folder, outputFile):
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".pp") and not os.path.islink(os.path.join(root, file)):
                fileObj = SourceModel.SM_File.SM_File(os.path.join(root, file))
                detectInsModForm2(fileObj, outputFile)

def detectInsModForm2(fileObj, outputFile):
    for aClass in fileObj.getOuterClassList():
        if aClass.getLocWithoutComments() > CONSTS.MAX_CLASS_LOC_THRESHOLD:
            Utilities.reportSmell(outputFile, fileObj.fileName, CONSTS.SMELL_INS_MOD_2, CONSTS.CLASS_RES)

    for aDefine in fileObj.getOuterDefineList():
        if aDefine.getLocWithoutComments() > CONSTS.MAX_DEFINE_LOC_THRESHOLD:
            Utilities.reportSmell(outputFile, fileObj.fileName, CONSTS.SMELL_INS_MOD_2, CONSTS.DEFINE_RES)

    if fileObj.getLinesOfCodeWithoutComments() > CONSTS.MAX_MODULE_LOC_THRESHOLD:
            Utilities.reportSmell(outputFile, fileObj.fileName, CONSTS.SMELL_INS_MOD_2, CONSTS.FILE_RES)

#Form 3 - When the complexity (max nesting depth) of a module is greater than a threshold
def detectInsufficientModForm3(folder, outputFile):
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".pp") and not os.path.islink(os.path.join(root, file)):
                fileObj = SourceModel.SM_File.SM_File(os.path.join(root, file))
                detectInsModForm3(fileObj, outputFile)

def detectInsModForm3(fileobj, outputFile):
    if fileobj.getMaxNestingDepth() > CONSTS.MAX_NESTING_DEPTH:
        Utilities.reportSmell(outputFile, fileobj.fileName, CONSTS.SMELL_INS_MOD_3, CONSTS.FILE_RES)

#Form 1 - size of the upper-level manifests folder when modules folder is absent, or both modules and manifests folder not present
def detectUnstructuredModForm1(folder, outputFile):
    if isModulesExists(folder):
        return
    manifestsFolder = getManifestsFolder(folder) #repo-level manifests folder
    if manifestsFolder == "":
        Utilities.reportSmell(outputFile, manifestsFolder, CONSTS.SMELL_UNS_MOD_1, CONSTS.REPO_MANIFEST)
        return
    if FileOperations.countPuppetFiles(manifestsFolder) > CONSTS.MAX_MANIFESTS_PUPPET_FILES:
        Utilities.reportSmell(outputFile, manifestsFolder, CONSTS.SMELL_UNS_MOD_1, CONSTS.REPO_MANIFEST)

def isModulesExists(folder):
    for aFile in os.listdir(folder):
        if os.path.isdir(os.path.join(folder,aFile)):
            if aFile.__contains__(CONSTS.MODULES):
                return True
    return False

def getModulesFolder(folder):
    for aFile in os.listdir(folder):
        if os.path.isdir(os.path.join(folder,aFile)):
            if aFile.__contains__(CONSTS.MODULES):
                return os.path.join(folder, aFile)
    return ""

def getManifestsFolder(folder):
    for aFile in os.listdir(folder):
        if os.path.isdir(os.path.join(folder,aFile)):
            if aFile == CONSTS.MANIFESTS:
                return os.path.join(folder, aFile)
    return ""

#Form 2 - In each module, manifest folder must be present
def detectUnstructuredModForm2(folder, outputFile):
    modulesFolder = getModulesFolder(folder)
    if modulesFolder:
        for dir in os.listdir(modulesFolder):
            if os.path.isdir(os.path.join(modulesFolder, dir)):
                detectUnsModForm2(os.path.join(modulesFolder, dir), outputFile)

def detectUnsModForm2(folder, outputFile):
    if not getManifestsFolder(folder):
        Utilities.reportSmell(outputFile, folder, CONSTS.SMELL_UNS_MOD_2, CONSTS.MODULE_MANIFEST)

#Form 3 - When a module contains other than recommended folders/files
def detectUnstructuredModForm3(folder, outputFile):
    modulesFolder = getModulesFolder(folder)
    if modulesFolder:
        for dir in os.listdir(modulesFolder):
            detectUnsModForm3(os.path.join(modulesFolder, dir), outputFile)

def detectUnsModForm3(folder, outputFile):
    counter = 0
    if os.path.isdir(folder):
        for dir in os.listdir(folder):
            if not (dir == "files" or dir == "manifests" or dir == "templates" or dir == "lib" or dir == "tests" or
                            dir == "spec" or dir.__contains__("readme") or dir.__contains__("README") or
                        dir.__contains__("license") or dir.__contains__("LICENSE") or dir.__contains__("metadata")):
                counter += 1

    if counter > CONSTS.MAX_ALLOWED_NONSTANDARD_FILES:
        Utilities.reportSmell(outputFile, folder, CONSTS.SMELL_UNS_MOD_3, CONSTS.OTHERFILES)

def detectTCMod(fileObj, outputFile):
    if not (fileObj.fileName.__contains__("param") or fileObj.fileName.__contains__("init") or fileObj.fileName.__contains__("site")):
        if len(fileObj.getHardCodedStatments()) > 1:
            Utilities.reportSmell(outputFile, fileObj.fileName, CONSTS.SMELL_TC_MOD, CONSTS.FILE_RES)

def getGraph(folder):
    graph = Graph.Graph.Graph()
    addGraphNodes(folder, graph)
    #graph.printGraph()
    addGraphEdges(folder, graph)
    return graph

def addGraphNodes(folder, graph):
    addGraphNodesFromModules(folder, graph)
    addGraphNodesFromRestPuppetFiles(folder, graph)

def addGraphNodesFromModules(folder, graph):
    modulesFolder = getModulesFolder(folder)
    if modulesFolder:
        for aDir in os.listdir(modulesFolder):
            aModule = os.path.join(modulesFolder, aDir)
            node = Graph.GraphNode.GraphNode(aModule)
            graph.addNode(node)
            addGraphResources(node, aModule)

def addGraphResources(node, aModule):
    if os.path.isdir(aModule):
        for root, dirs, files in os.walk(aModule):
            for file in files:
                if file.endswith(".pp") and not os.path.islink(os.path.join(root, file)):
                    fileObj = SourceModel.SM_File.SM_File(os.path.join(root, file))
                    addResources(fileObj, node)
    else:
        if aModule.endswith(".pp") and not os.path.islink(aModule):
            fileObj = SourceModel.SM_File.SM_File(aModule)
            addResources(fileObj, node)


def addResources(fileObj, node):
    for item in fileObj.getFileResourceList():
        node.addResource(item.getResourceName(), GRCONSTS.FILE)
    for item in fileObj.getPackageResourceList():
        node.addResource(item.getResourceName(), GRCONSTS.PACKAGE)
    for item in fileObj.getServiceResourceList():
        node.addResource(item.getResourceName(), GRCONSTS.SERVICE)
    for item in fileObj.getClassDeclarationList():
        node.addResource(item.getResourceName(), GRCONSTS.CLASS)


def addGraphNodesFromRestPuppetFiles(folder, graph):
    for root, dirs, files in os.walk(folder):
        #remove the modules folder for this method (we are already done with it )
        for aDir in dirs:
            if aDir.__contains__(CONSTS.MODULES):
                dirs.remove(aDir)

        for file in files:
            if file.endswith(".pp"):
                aFile = os.path.join(root, file)
                node = Graph.GraphNode.GraphNode(aFile)
                graph.addNode(node)
                addGraphResources(node, aFile)

def addGraphEdges(folder, graph):
    addGraphEdgesFromModules(folder, graph)
    addGraphEdgesFromRestPuppetFiles(folder, graph)

def addGraphEdgesFromModules(folder, graph):
    modulesFolder = getModulesFolder(folder)
    if modulesFolder:
        for aDir in os.listdir(modulesFolder):
            aModule = os.path.join(modulesFolder, aDir)
            node = graph.getNodeWithId(aModule)
            if node:
                addGraphEdgesByNode(node, graph, aModule)

def addGraphEdgesByNode(node, graph, aModule):
    if os.path.isdir(aModule):
        for root, dirs, files in os.walk(aModule):
            for file in files:
                if file.endswith(".pp") and not os.path.islink(os.path.join(root, file)):
                    fileObj = SourceModel.SM_File.SM_File(os.path.join(root, file))
                    addEdges(fileObj, node, graph)
    else:
        if aModule.endswith(".pp") and not os.path.islink(aModule):
            fileObj = SourceModel.SM_File.SM_File(aModule)
            addEdges(fileObj, node, graph)

def addEdges(fileObj, node, graph):
    for item in fileObj.getFileResourceList():
        for name, type in item.getDependentResource():
            dependentNode = searchDependentNode(graph, node, name, type)
            if dependentNode:
                if not dependentNode == node:
                    graph.addEdge(node, dependentNode)

    for item in fileObj.getServiceResourceList():
        for name, type in item.getDependentResource():
            dependentNode = searchDependentNode(graph, node, name, type)
            if dependentNode:
                if not dependentNode == node:
                    graph.addEdge(node, dependentNode)

    for item in fileObj.getPackageResourceList():
        for name, type in item.getDependentResource():
            dependentNode = searchDependentNode(graph, node, name, type)
            if dependentNode:
                if not dependentNode == node:
                    graph.addEdge(node, dependentNode)

    for item in fileObj.getClassDeclarationList():
        for name, type in item.getDependentResource():
            dependentNode = searchDependentNode(graph, node, name, type)
            if dependentNode:
                if not dependentNode == node:
                    graph.addEdge(node, dependentNode)

def searchDependentNode(graph, node, name, type):
    #print("Looking for Name: " + name + " Type: " + type)
    for res in node.getResources():
        if res.name == name and res.type == type:
            node.addInternalDependency()
            #print("found")
            return node

    for aNode in graph.getNodes():
        for res in aNode.getResources():
            if res.name == name and res.type == type:
                #print("Found")
                node.addExternalDependency()
                return aNode
    #Okay, so we have not found the node i.e. it is an external dependency.
    #In this case, we will create a graph node to capture the dependency.
    newNode = Graph.GraphNode.GraphNode(name)
    newNode.addResource(name, type)
    graph.addNode(newNode)
    node.addExternalDependency()
    #print("Found_New")
    return newNode

def addGraphEdgesFromRestPuppetFiles(folder, graph):
    for root, dirs, files in os.walk(folder):
        #remove the modules folder for this method (we are already done with it )
        for aDir in dirs:
            if aDir.__contains__(CONSTS.MODULES):
                dirs.remove(aDir)

        for file in files:
            if file.endswith(".pp"):
                aFile = os.path.join(root, file)
                node = graph.getNodeWithId(aFile)
                if node:
                    addGraphEdgesByNode(node, graph, aFile)

def detectHaiStr(graph, folder, outputFile):
    if graph.getAverageDegree() > CONSTS.MAX_GRAPH_DEGREE_THRESHOLD:
        Utilities.reportSmell(outputFile, folder, CONSTS.SMELL_HAI_STR, CONSTS.REPO_RES)

def detectWeakendMod(graph, folder, outputFile):
    for node in graph.getNodes():
        if node.getModularityRatio() < CONSTS.MODULARITY_THRESHOLD:
            Utilities.reportSmell(outputFile, str(node.getId()), CONSTS.SMELL_WEA_MOD, CONSTS.MODULE_RES)
