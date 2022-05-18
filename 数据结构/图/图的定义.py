# 采用邻接表实现图
class Node:
    def __init__(self, id=0, val=0, neighbors=None):
        self.id = id  # 结点索引
        self.val = val  # 结点值
        self.neighbors = neighbors if neighbors is not None else {}  # 邻接结点，键为结点索引，值为权重
    
    def addNeighbor(self, nbrid, weight=0):
        self.neighbors[nbrid] = weight


class Graph:
    def __init__(self):
        self.nodes = {}  # 结点表，键为结点索引，值为 Node
    
    def addNode(self, id, val=0):
        new_node = Node(id, val)
        self.nodes[id] = new_node
    
    def addEdge(self, id, nbrid, weight=0):
        if id not in self.nodes.keys():
            self.addNode(id)
        if nbrid not in self.nodes.keys():
            self.addNode(nbrid)
        self.nodes[id].addNeighbor(nbrid, weight)