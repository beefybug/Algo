import os
import sys
# graph might be in parent directory
try:
    import graph
except ImportError:
    sys.path.append("..")
    import graph


def analyze(inFile, outFile):
    with open(inFile, 'r') as f:
        data = []
        numV = int(f.readline().split(" ")[0])
        for line in f:
            data.append(list(map(int, line.split(' '))))

    g = graph.graph(numV, data)
    d = graph.DFS(g)
    d.SCC()
    g.SCC()
    print(d.groups == g.groups)  # Check that my solution is same as builtin
    with open(outFile, 'w') as f:
        f.write("{}\n".format(len(d.groups)))
        for g in d.groups:
            outString = "{} {}".format(len(g), " ".join(map(str, g)))
            f.write(outString + '\n')


# Assumes that inputs are in the same folder as HW2.py
for root, directories, files in os.walk(sys.path[0]):
    for filename in files:
        if filename.lower().endswith(".txt") and \
                filename.lower().startswith("in"):
            inFile = os.path.join(root, filename)
            outFile = os.path.join(root, filename.replace("in", "out"))
            analyze(inFile, outFile)
