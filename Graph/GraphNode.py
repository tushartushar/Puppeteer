import Graph.Resource

class GraphNode:
    def __init__(self, id):
        self.resourceList = []
        self.id = id

    def addResource(self, resourceName, resourceType):
        self.resourceList.append(Graph.Resource.Resource(resourceName, resourceType))
        #print("Adding resource Name: " + resourceName + " resource Type: " + resourceType)

    def getResources(self):
        return self.resourceList