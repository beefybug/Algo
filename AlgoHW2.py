import graph
import os
import sys


def analyze(filename):
    with open(filename, 'r') as f:
        data = []
        numV = int(f.readline().split(" ")[0])
        for line in f:
            data.append(list(map(int, line.split(' '))))

    g = graph.graph(numV, data)
    d = graph.DFS(g)
    d.SCC()

    filename = filename.replace("Input", "Output")
    with open(filename, 'w') as f:
        f.write("{}\n".format(len(d.groups)))
        for g in d.groups:
            f.write("{} {}\n".format(len(g), " ".join(map(str, g))))


# Assumes that inputs are in the "Input" folder and same directory as this py
for root, directories, files in os.walk(os.path.join(sys.path[0], "Input")):
    for filename in files:
        fullpath = os.path.join(root, filename)
        if fullpath.lower().endswith(".txt"):
            print(fullpath)
            analyze(fullpath)
