import os
import sys
try:
    import graph
except ImportError:
    sys.path.append("..")
    import graph


def analyze(filename):
    with open(filename, 'r') as f:
        data = []
        numV = int(f.readline().split(" ")[0])
        for line in f:
            data.append(list(map(int, line.split(' '))))

    g = graph.graph(numV, data)
    d = graph.DFS(g)
    d.SCC()
    g.SCC()

    filename = filename.replace("in", "out")
    with open(filename, 'w') as f:
        f.write("{}\n".format(len(d.groups)))
        for g in d.groups:
            outString = "{} {}".format(len(g), " ".join(map(str, g)))
            f.write(outString + '\n')
            print(outString)


# Assumes that inputs are in the "Input" folder and same directory as this py
for root, directories, files in os.walk(sys.path[0]):
    for filename in files:
        fullpath = os.path.join(root, filename)
        if fullpath.lower().endswith(".txt"):
            print(fullpath)
            analyze(fullpath)
