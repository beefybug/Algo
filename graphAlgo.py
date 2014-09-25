from collections import deque


# Trick for creating enums in python
def enum(*sequential, **named):
    enums = dict(zip(sequential, range(len(sequential))), **named)
    return type('Enum', (), enums)


# graph_type = enum("Directed", "Undirected")
# store_type = enum("Adj_Matrix", "Adj_List")

# TODO create data structure to represent search trees.


class graph:

    def __init__(self, num_V, E):
        self.numV = num_V
        self.numE = len(E)
        self.initEV(num_V, E)

    def initEV(self, num_V, E):
        """E should be passed as a tuple of tuple with the assumption that
        the directon is u -> v for (u, v). Does not matter for undirected.
        All entries in E should be unique.
        """

        self.outData = [[] for i in range(num_V)]
        self.inData = [[] for i in range(num_V)]
        for pair in E:
            self.outData[pair[0]].append(pair[1])
            self.inData[pair[1]].append(pair[0])

        for i in self.outData:
            i.sort()

        for j in self.inData:
            j.sort()


class BFS:

    def __init__(self, g):
        self.graph = g
        self.discovered = [0 for i in range(g.numV)]
        self.distance = [0 for i in range(g.numV)]
        self.parent = [0 for i in range(g.numV)]

    def run(self, start):
        if start < 0 or start >= self.graph.numV:
            raise ValueError("The starting vertex is out of range.")
        self.startingVertex = start
        self.parent[start] = 's'
        self.discovered[start] = 1
        queue = deque([start])

        while len(queue) > 0:
            u = queue.popleft()
            for v in self.graph.outData[u]:
                # v refers to neighbours of u
                if self.discovered[v] == 0:
                    self.discovered[v] = 1
                    queue.append(v)
                    self.distance[v] = self.distance[u] + 1
                    self.parent[v] = u

    def __str__(self):
        line = "Parent  :{}\n".format(self.parent)
        line += "Distance:{}".format(self.distance)
        return line


class DFS:

    def __init__(self, g):
        self.cnt = 1
        self.graph = g
        self.discovered = [0 for i in range(g.numV)]
        self.start = [0 for i in range(g.numV)]
        self.finish = [0 for i in range(g.numV)]

    def run(self):
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

    def __str__(self):
        line = "Start time :{}\n".format(self.start)
        line += "Finish time:{}".format(self.finish)
        return line


def test():
    E = ((0, 1),
         (1, 2),
         (2, 0),
         (0, 3),
         (4, 3),
         (4, 5),
         (5, 6),
         (6, 4))
    num_V = 7
    g = graph(num_V, E)
    print(g.inData)
    print(g.outData)
    b = BFS(g)
    b.run(6)
    print(b)
    d = DFS(g)
    d.run()
    print(d)

test()
