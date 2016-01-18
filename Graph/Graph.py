
class Graph:
    def __init__(self):
        self.dict = dict()

    def addNode(self, node):
        if not self.dict.__contains__(node):
            self.dict[node] = []

    def getNodeCount(self):
        return len(self.dict)

    def addEdge(self, node1, node2):
        if self.dict.__contains__(node1) and self.dict.__contains__(node2):
            if not self.dict[node1].__contains__(node2):
                self.dict[node1].append(node2)

    def getEdgeCount(self):
        counter = 0
        for item in self.dict:
            if self.dict[item]:
                counter += len(self.dict[item])
        return counter

    def printGraph(self):
        for item in self.dict.keys():
            print ("key: " + str(item) + " value: " + str(self.dict[item]))

    def getNodeWithId(self, id):
        for node in self.dict.keys():
            if node.id == id:
                return node

    def getNodes(self):
        return self.dict.keys()

    def getAverageDegree(self):
        totalEdges = self.getEdgeCount()
        totalNodes = len(self.dict.keys())
        if totalNodes == 0:
            return float(0)
        else:
            return float(totalEdges * 2)/float(totalNodes)
