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

    def read(self, v): #graph.read([])
        self.data = v
        self.size = len(v)

    def findMinimum(self, E):
        val = E[0]
        for i in range(len(E)):
            if val[2] > E[i][2]:
                val = E[i]
        return val

    def process(self):
        #array hold all vertices
        T = [False] * self.size #[False, False, False, False]
        #array of edges
        L = [] # [vertexIdA, vertexIdB, weight]
        E = []
        #do the algorithm
        for i in range(self.size):
            if i == 0:
                #One to be Selected
                T[i] = True
            else:
                for j in range(self.size):
                    for k in range(j, self.size):
                        if T[j] != T[k]:
                            E.append([j, k, self.data[j][k]])
                targetEdge = self.findMinimum(E)
                L.append(targetEdge)
                T[targetEdge[0]] = True
                T[targetEdge[1]] = True
                E = []

        #print(L)
        length = 0
        for ele in L:
            length += ele[2]
        print("Minimum Spanning Tree Length is:", length)

g = Graph()
g.readFromCSV('graph.csv')
# g.read(
#     [
#         [0, 2, 6, 12],
#         [2, 0, 10, 5],
#         [6, 10, 0, 4],
#         [12, 5, 4, 0]
#     ]
# )

g.process()
