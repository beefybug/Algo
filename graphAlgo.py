from collections import deque


# Trick for creating enums in python
def enum(*sequential, **named):
    enums = dict(zip(sequential, range(len(sequential))), **named)
    return type('Enum', (), enums)


graph_type = enum("Directed", "Undirected")
store_type = enum("Adj_Matrix", "Adj_List")

# TODO create data structure to represent search trees.


class graph:

    def __init__(self, num_V=None, E=None, gt=None, st=store_type.Adj_List):
        self.numV = num_V
        self.numE = len(E)
        self.graph = gt
        self.store = st
        self.initEV(num_V, E, st)

    def initEV(self, num_V, E, st):
        """E should be passed as a tuple of tuple with the assumption that
        the directon is u -> v for (u, v). Does not matter for undirected.
        E should be unique as well.
        """

        if st == store_type.Adj_List:
            self.outData = [[] for i in range(num_V)]
            self.inData = [[] for i in range(num_V)]
            for pair in E:
                self.outData[pair[0]].append(pair[1])
                self.inData[pair[1]].append(pair[0])


def BFS(g, start):
    """Breath First Search of a graph starting from vertex start"""
    size_of_V = g.numV
    if start < 0 or start >= size_of_V:
        raise ValueError("The starting vertex is out of range.")
    # Initialization of counters
    discovered = [0 for i in range(size_of_V)]
    discovered[start] = 1
    distance = [0 for i in range(size_of_V)]
    parent = [None for i in range(size_of_V)]
    parent[start] = -1

    # Uses built-in queue definitio
    queue = deque([start])
    while len(queue) > 0:
        u = queue.popleft()
        for v in g.outData[u]:
            # v refers to neighbours of u
            if discovered[v] == 0:
                discovered[v] = 1
                queue.append(v)
                distance[v] = distance[u] + 1
                parent[v] = u

    print("Parents :", parent)
    print("Distance:", distance)


def DFS(g, start):
    """Depth First Search of a graph starting from vertex start"""
    size_of_V = g.numV
    if start < 0 or start >= size_of_V:
        raise ValueError("The starting vertex is out of range.")

    discovered = [0 for i in range(size_of_V)]
    discovered[start] = 1
    distance = [0 for i in range(size_of_V)]
    parent = [0 for i in range(size_of_V)]
    parent[start] = None
    # TODO need to complete the DFS algorithm


def search(g, vertex):
    # TODO write the recursive search function
    pass


def printAtt(obj):
    for i in dir(obj):
        if i[0] != '_':
            print(i, getattr(obj, i))


def test():
    E = ((0, 2),
         (0, 4),
         (0, 5),
         (1, 0),
         (2, 1),
         (2, 5),
         (3, 1),
         (3, 6),
         (4, 0),
         (4, 5),
         (6, 3),
         (6, 5))
    num_V = 7
    a = graph(num_V, E, graph_type.Directed, store_type.Adj_List)
    print(a.inData)
    print(a.outData)
    BFS(a, 6)

test()
