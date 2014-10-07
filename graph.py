from collections import deque
from copy import copy
import networkx as nx


class graph:

    def __init__(self, num_V, E):
        self.numV = num_V
        self.numE = len(E)
        self.G = nx.DiGraph()
        self.G.add_nodes_from([i for i in range(1, num_V+1)])
        self.initEV(num_V, E)

    def initEV(self, num_V, E):
        """E should be passed as a tuple of tuple with the assumption that
        the directon is u -> v for (u, v). All entries in E should be unique.
        """

        # TODO account for weight
        self.outData = [[] for i in range(num_V)]
        self.inData = [[] for i in range(num_V)]
        # Vertex is 1-indexed but storage is 0-indexed
        try:
            for pair in E:
                self.outData[pair[0]-1].append(pair[1]-1)
                self.inData[pair[1]-1].append(pair[0]-1)
                self.G.add_edge(*pair)
        except IndexError as e:
            print("Issue at pair {}".format(pair))
            raise e

    def SCC(self):
        # Used to compare result with those from DFS algo
        self.groups = [sorted(i)
                       for i in nx.strongly_connected_components(self.G)]
        self.groups.sort()


class BFS:

    def __init__(self, g):
        self.graph = g
        self.discovered = [0 for i in range(g.numV)]
        self.distance = [0 for i in range(g.numV)]
        self.parent = [0 for i in range(g.numV)]

    def run(self, start):
        if start < 0 or start > self.graph.numV:
            raise ValueError("The starting vertex is out of range.")
        self.startingVertex = start
        self.parent[start-1] = 's'
        self.discovered[start-1] = 1
        queue = deque([start-1])

        while len(queue) > 0:
            u = queue.popleft()
            for v in self.graph.outData[u]:
                # v refers to neighbours of u and accounted for 0-indexed
                if self.discovered[v] == 0:
                    self.discovered[v] = 1
                    queue.append(v)
                    self.distance[v] = self.distance[u] + 1
                    self.parent[v] = u + 1

    def __str__(self):
        line = "Parent  :{}\n".format(self.parent)
        line += "Distance:{}".format(self.distance)
        return line


class DFS:

    def __init__(self, g):
        self.graph = g
        self.discovered = None
        self.start = None
        self.finish = None
        self.groups = None

    def run(self):
        self.cnt = 1
        self.discovered = [0 for i in range(self.graph.numV)]
        self.start = [0 for i in range(self.graph.numV)]
        self.finish = [0 for i in range(self.graph.numV)]
        for u in range(self.graph.numV):
            if self.discovered[u] == 0:
                self.search(u)

    def search(self, u):
        self.previsit(u)
        self.discovered[u] = 1
        for v in self.graph.outData[u]:
            if self.discovered[v] == 0:
                self.search(v)
        self.postvisit(u)

    def previsit(self, u):
        self.start[u] = self.cnt
        self.cnt += 1

    def postvisit(self, u):
        self.finish[u] = self.cnt
        self.cnt += 1

    def SCC(self):
        if self.start is None:
            self.run()  # Ensure that finish time is available

        self.groups = []
        self.temp = copy(self.finish)
        # After exploring a node, the finish time for it is set to 0,
        while sum(self.temp) > 0:
            self.groups.append([])
            u = self.temp.index(max(self.temp))
            self.searchSCC(u)

        for group in self.groups:
            group.sort()

        self.groups.sort()

    def searchSCC(self, u):
        self.groups[-1].append(u + 1)
        self.discovered[u] = 0
        self.temp[u] = 0
        for v in self.graph.inData[u]:
            if self.discovered[v] == 1:
                self.searchSCC(v)

    def printGroups(self):
        for idx, g in enumerate(self.groups):
            print(len(g), g)
            # Checking to make sure that it is sorted
            if idx > 0 and self.groups[idx][0] < self.groups[idx-1][0]:
                raise ArithmeticError

    def __str__(self):
        line = "Start time :{}\n".format(self.start)
        line += "Finish time:{}".format(self.finish)
        return line


def _test():
    E = ((1, 2),
         (2, 3),
         (3, 4),
         (5, 1),
         (2, 5),
         (2, 6),
         (8, 4),
         (5, 6),
         (6, 7),
         (4, 3),
         (7, 6),
         (8, 7),
         (4, 8))
    num_V = 8
    g = graph(num_V, E)
    d = DFS(g)
    d.SCC()
    d.printGroups()
    g.SCC()

if __name__ == "__main__":
    _test()
