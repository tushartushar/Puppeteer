from unittest import TestCase
import Graph.Graph
import Graph.GraphNode
import Graph.GR_Constants as GRCONSTS

class TestGraph(TestCase):
    def test_addNode(self):
        graph = Graph.Graph.Graph()
        node = Graph.GraphNode.GraphNode("1")
        node.addResource("apache", GRCONSTS.PACKAGE)
        graph.addNode(node)
        self.assertEquals(graph.getNodeCount(), 1)

    def test_addEdge(self):
        graph = Graph.Graph.Graph()
        node1 = Graph.GraphNode.GraphNode("1")
        node2 = Graph.GraphNode.GraphNode("2")
        graph.addNode(node1)
        graph.addNode(node2)
        graph.addEdge(node1, node2)
        graph.printGraph()
        self.assertEquals(graph.getEdgeCount(), 1)