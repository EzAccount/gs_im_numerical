import time
from collections import defaultdict
import numpy as np

class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.org_graph = [i[:] for i in graph]
        self. ROW = len(graph)
        self.COL = len(graph[0])

    def BFS(self,s, t, parent):
        visited =[False]*(self.ROW)
        queue=[]
        queue.append(s)
        visited[s] = True
        while queue:
            u = queue.pop(0)
            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0 :
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u

        return True if visited[t] else False

    def minCut(self, source, sink):
        parent = [-1]*(self.ROW)

        max_flow = 0
        while self.BFS(source, sink, parent) :
            path_flow = float("Inf")
            s = sink
            while(s !=  source):
                path_flow = min (path_flow, self.graph[parent[s]][s])
                s = parent[s]
            max_flow +=  path_flow
            v = sink
            while(v !=  source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]
        print ("Energy", E-max_flow-max_flow)


start = time.time()
h = []

with open("fields.txt") as f:
    for line in f:
        h.append(float(line))
read = time.time()
graph = [[0]*(len(h)+2) for x in range(len(h)+2)]
for i in range(len(h)):
    if (h[i]>0): graph[0][i+2]=h[i];
    if (h[i]<0): graph[i+2][1]=-h[i];
    if (i>0):
        graph[i+2][i+1] = 1.0
        graph[i+1][i+2] = 1.0

g = Graph(graph)

graphed = time.time()

size=len(graph)
E = sum(sum(graph[i][-size+i:]) for i in range(size)) + sum(graph[i][1] for i in range(size))
source = 0; sink =  1


g.minCut(source, sink)
done = time.time()
with open("time.txt", "a") as f:
    f.write("Small fields, 1E3:\n")
    f.write("Max Flow - Min Cut algorithm:\n")
    f.write("File processing: "+str(read-start)+str('\n'))
    f.write("Graph constructing: "+str(graphed-read)+str('\n'))
    f.write("maxflow-mincut problem: "+str(done-graphed)+str('\n'))
    f.write("Total: "+str(done-start)+str('\n'))
