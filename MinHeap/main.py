# Driver program to test the above functions
from Graph import *

graph = Graph(0)
graph.readFromCSV('graph.csv')
graph.PrimMST()