#######################################################################################################################
# AUTHOR - KODY JOHNSON (1209950115)
# DATE - 11/30/19
# CLASS - CSE450
# PROJECT - PROJECT 1
#######################################################################################################################

from sys import exit
from collections import deque
from datetime import timedelta, time

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


# Node
class Node:

    def __init__(self, airline, start, end, arrival, departure, aircraft):
        self.airline = airline
        self.start = start
        self.end = end
        self.arrival = arrival
        self.departure = departure
        self.aircraft = aircraft


class Graph:

    @staticmethod
    def round_time(t):
        # convert to datetime.time object
        t = time(hour=int(t[0:2]), minute=int(t[2:4]))
        # round to nearest hour
        if t.minute >= 30:
            return t.replace(minute=0, hour=t.hour+1)
        else:
            return t.replace(minute=0)

    @staticmethod
    def aircraft_to_capacity(aircraft):
        if aircraft == 'A220':
            aircraft = 105
        elif aircraft == 'A319':
            aircraft = 128
        elif aircraft == 'A320':
            aircraft = 150
        elif aircraft == 'A321':
            aircraft = 185
        elif aircraft == '717200':
            aircraft = 110
        elif aircraft == '737700':
            aircraft = 126
        elif aircraft == '737800':
            aircraft = 165
        elif aircraft == '737900':
            aircraft = 180
        elif aircraft == '757200':
            aircraft = 180
        elif aircraft == '757300':
            aircraft = 230
        elif aircraft == '767300':
            aircraft = 200
        elif aircraft == '777200':
            aircraft = 270
        elif aircraft == '777200LR':
            aircraft = 280
        elif aircraft == '787800':
            aircraft = 235
        elif aircraft == 'E170':
            aircraft = 72
        elif aircraft == 'E175':
            aircraft = 78
        elif aircraft == 'MD88':
            aircraft = 150
        elif aircraft == 'MD90':
            aircraft = 150
        elif aircraft == 'RJ700':
            aircraft = 75
        elif aircraft == 'RJ900':
            aircraft = 75
        elif aircraft == 'RJ175':
            aircraft = 78
        return aircraft

    def read_input_file(self):
        f = open(FILE)
        new_node = Node
        nodeList = []
        for line in f:
            split1 = line.split(':')
            new_node.airline = split1[0]
            new_node.start = split1[1]
            new_node.end = split1[2]
            new_node.arrival = self.round_time(split1[3])
            new_node.departure = self.round_time(split1[4])
            new_node.aircraft = self.aircraft_to_capacity(split1[5].strip())
            #print("Airline", new_node.airline, "Start:", new_node.start, "End:", new_node.end, "Arrival:", new_node.arrival,
            #      "Departure:", new_node.departure, "Aircraft:", new_node.aircraft)
            nodeList.append(new_node)

        return nodeList

    # So this is Breadth-First-Search or BFS that will return true if a path exists from the s to t.
    def BFS(self, s, t, parent):
        visited = [False] * self.ROW
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
        parent = [-1] * self.ROW
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
    # Must depart and arrive on above date within 24 hours.
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
    graphMNG = Graph()
    test = graphMNG.read_input_file()
    source_ = 0
    sink_ = 654

    # print("The maximum capacity is", g.maximum_Flow(source_, sink_))
    exit(0)
