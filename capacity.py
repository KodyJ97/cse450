#######################################################################################################################
# AUTHOR - KODY JOHNSON (1209950115)
# DATE - 11/30/19
# CLASS - CSE450
# PROJECT - PROJECT 1
#######################################################################################################################

from sys import exit
from collections import deque
class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.ROW = len(graph)

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
    # TBA
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
    # 10 cities = 10 nodes
    # each node has a city, arrival time, departure time, and edge weights or capacities of the aircraft type.
    graph_ = [[0, 16, 13, 0, 0, 0],
              [0, 0, 10, 12, 0, 0],
              [0, 4, 0, 0, 14, 0],
              [0, 0, 9, 0, 0, 20],
              [0, 0, 0, 7, 0, 4],
              [0, 0, 0, 0, 0, 0]]
    g = Graph(graph_)
    source_ = 0
    sink_ = 5
    print("The maximum flow possible is", g.maximum_Flow(source_, sink_))
    exit(0)
