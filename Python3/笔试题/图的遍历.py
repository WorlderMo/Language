# -*- coding: utf-8 -*-
# @Date    : 2018-09-06 20:13:25
# @Author  : mohailang (1198534595@qq.com)


class Vertex(object):
    def __init__(self, key):
        self.ID = key
        self.connectedTo = {}

    def addNeighbor(self, nbr, weight=None):
        self.connectedTo[nbr] = weight

    def getConnections(self):
        return self.connectedTo.keys()

    def getID(self):
        return self.ID


class Graph(object):

    def __init__(self):
        self.vertexList = {}
        self.vertexNum = 0

    def addVertex(self, key):
        self.vertexNum += 1
        newVertex = Vertex(key)
        self.vertexList[key] = newVertex
        return newVertex

    def addEdge(self, vertex1, vertex2, weight=1):
        """连接两个顶点：vertex1->vertex2"""
        if vertex1 not in self.vertexList:
            self.addVertex(vertex1)
        if vertex2 not in self.vertexList:
            self.addVertex(vertex2)
        self.vertexList[vertex1].addNeighbor(self.vertexList[vertex2], weight)

    dfsVisited = []

    def dfs(self, root):

        connections = self.vertexList[root].getConnections()
        if root not in self.dfsVisited:
            self.dfsVisited.append(root)
            # print(root, end=' ')
            for neighbor in connections:
                self.dfs(neighbor.getID())
            self.dfsVisited.append(root)
        return self.dfsVisited


if __name__ == '__main__':
    graph = Graph()
    N = int(input())
    for i in range(N-1):
        nums = list(map(int, input().split()))
        graph.addEdge(nums[0], nums[1])
    print(len(graph.dfs(1))//2)
