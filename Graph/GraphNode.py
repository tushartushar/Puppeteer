import Graph.Resource

class GraphNode:
    def __init__(self, id):
        self.resourceList = []
        self.id = id
        self.internalDep = 0
        self.externalDep = 0

    def addResource(self, resourceName, resourceType):
        self.resourceList.append(Graph.Resource.Resource(resourceName, resourceType))
        #print("Adding resource Name: " + resourceName + " resource Type: " + resourceType)

    def getResources(self):
        return self.resourceList

    def getId(self):
        return self.id

    def getModularityRatio(self):
        if self.externalDep == 0:
            return 1
        return float(str("{:.2f}".format((float(self.internalDep)/float(self.externalDep)))))

    def addInternalDependency(self):
        self.internalDep += 1

    def addExternalDependency(self):
        self.externalDep += 1