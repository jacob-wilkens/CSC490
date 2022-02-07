import csv

class Graph:
    def __init__(self):
        pass

    def readFromCSV(self, fileName):
        data = list(csv.reader(open(fileName)))
        for i in range(len(data)):
            for j in range(len(data[i])):
                data[i][j] = int(data[i][j])

        self.data = data
        self.size = len(self.data)

    def read(self, v):  # graph.read([])
        self.data = v
        self.size = len(v)

    def findMinimum(self, E):
        return sorted(E, key=lambda x: x[2])[0]

    @profile
    def process(self):
        # array hold all vertices
        T = [False] * self.size  # [False, False, False, False]
        # array of edges
        L = []  # [vertexIdA, vertexIdB, weight]
        E = []
        # do the algorithm
        T[0] = True
        for i in range(1, self.size):
            for j in range(self.size):
                for k in range(j, self.size):
                    if T[j] != T[k]:
                        E.append([j, k, self.data[j][k]])
            targetEdge = self.findMinimum(E)
            L.append(targetEdge)
            T[targetEdge[1]] = True
            E = []

        length = 0
        for ele in L:
            length += ele[2]
        print("Minimum Spanning Tree Length is:", length)

g = Graph()
g.readFromCSV('graph.csv')
g.process()
