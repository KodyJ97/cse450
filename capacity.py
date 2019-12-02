#######################################################################################################################
# AUTHOR - KODY JOHNSON (1209950115)
# DATE - 11/30/19
# CLASS - CSE450
# PROJECT - PROJECT 1
#######################################################################################################################

from sys import exit
from collections import deque

# Data File
FILE = '/home/kody/myrepos/cse450/450_data.txt'

# Plane Capacities
A220 = 105
A319 = 128
A320 = 150
A321 = 185
A321neo = 196
A330_200 = 230
A330_300 = 290
A330_900neo = 280
A350_900 = 300
B717_200 = 110
B737_700 = 126
B737_800 = 165
B737_900 = 180
B737_900ER = 180
B737_Max9 = 180
B757_200 = 180
B757_300 = 230
B767_300 = 200
B767_300ER = 225
B767_400ER = 240
B777_200 = 270
B777_200ER = 270
B777_200LR = 280
B777_300 = 300
B787_8 = 235
B787_9 = 280
Embraer170 = 72
Embraer175_E75 = 78
Embraer190 = 100
McDonnellDouglasMD_88 = 150
McDonnellDouglasMD_90_30 = 150
CRJ700 = 75
CRJ900 = 75

class Graph:

    def __init__(self, graph):
        self.graph = graph
        self.ROW = len(graph)

    @staticmethod
    def read_input_file():
        f = open(FILE)
        return 1

    # So this is Breadth-First-Search or BFS that will return true if a path exists from the s to t.
    def BFS(self, s, t, parent):
        visited = [False]*self.ROW
        queue = deque()
        queue.append(s)
        visited[s] = True

        while queue:

            # Remove left most vertex
            u = queue.popleft()
            print("Vertex Removed", u)

            # Retrieve all adjacent vertices and if a adjacent vertex has not been visited we will make it visited
            # then enqueue it.
            for ind, val in enumerate(self.graph[u]):
                if visited[ind] is False and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u

        return True if visited[t] else False

    # Sources for this algorithm are wikipedia, geeksforgeeks, and lessons in class.
    def maximum_Flow(self, source, sink):
        # Parent array will be filled in the BFS and is storing the path.
        parent = [-1]*self.ROW
        # max flow initialized to zero
        max_flow = 0

        # While there is a path from s to t on graph_c keep going.
        while self.BFS(source, sink, parent):

            # path_flow is an unbounded upper value for comparisons..
            path_flow = float("Inf")
            s = sink
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            max_flow += path_flow

            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow

if __name__ == '__main__':
    # Notes
    # Date --------------------------
    # January 6th, 2020
    # Must depart and arrive on above date.
    # Aircraft Type -----------------
    # 737 - 165
    # 32b - 185
    # 321 - 185
    #767-300  200
    # Cities ------------------------
    # LAX-Los Angeles
    # SFO-San Francisco
    # PHX-Phoenix
    # SEA-Seattle
    # DEN-Denver
    # ATL-Atlanta
    # ORD-Chicago
    # BOS-Boston
    # IAD-Washington DC
    # JFK-New York
    # Airlines ----------------------
    # AA-American
    # DL-Delta
    # UA-United
    # Hard code data into graph.
    # Nodes =
    # Each node represent a time and city
    graph_ = [[0, 16, 13, 0, 0, 0],
              [0, 0, 10, 12, 0, 0],
              [0, 4, 0, 0, 14, 0],
              [0, 0, 9, 0, 0, 20],
              [0, 0, 0, 7, 0, 4],
              [0, 0, 0, 0, 0, 0]]
    new_graph = Graph.read_input_file()
    g = Graph(graph_)
    source_ = 0
    sink_ = 5
    print("The maximum capacity is", g.maximum_Flow(source_, sink_))
    exit(0)
