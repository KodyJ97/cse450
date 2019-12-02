#######################################################################################################################
# AUTHOR - KODY JOHNSON (1209950115)
# DATE - 11/30/19
# CLASS - CSE450
# PROJECT - PROJECT 1
#######################################################################################################################

from sys import exit
from collections import deque
from datetime import time

# Data File
FILE = '/home/kody/myrepos/cse450/450_data.txt'

# Node
class Node:

    def __init__(self, airline, start, end, departure, arrival, aircraft):
        self.airline = airline
        self.start = start
        self.end = end
        self.departure = departure
        self.arrival = arrival
        self.aircraft = aircraft

class Graph:

    # Print flight info - helper function not part of actual project.
    @staticmethod
    def print_flight(flight):
        print("Airline:", flight.airline, "Start:", flight.start, "End:", flight.end, "Departure:", flight.departure, "Arrival:", flight.arrival,  "Aircraft Capacity:", flight.aircraft)

    # Round the times - There is an error in here with times at 12:30 to 12:59 being rounded to 13 ---------------------
    @staticmethod
    def round_time(t):
        # convert to datetime.time object
        t = time(hour=int(t[0:2]), minute=int(t[2:4]))
        # round to nearest hour
        if t.minute >= 30:
            return t.replace(minute=0, hour=t.hour+1)
        else:
            return t.replace(minute=0)

    # Convert aircraft type to corresponding capacity.
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

    # Analyze all flights that end in JFK because these are all our valid flights that we want.
    @staticmethod
    def valid_flight(flights):
        flights_JFK = []
        for flight in flights:
            if flight.end == 'JFK':
                flights_JFK.append(flight)
        return flights_JFK

    # Read, parse, and store data.
    def read_input_file(self):
        f = open(FILE)
        new_node = Node
        nodeList = []
        # Parse the file using the ':' delimiter
        for line in f:
            split1 = line.split(':')
            new_node.airline = split1[0]
            new_node.start = split1[1]
            new_node.end = split1[2]
            new_node.departure = str(self.round_time(split1[3])) + split1[3][4:5] + 'M'
            new_node.arrival = str(self.round_time(split1[4])) + split1[4][4:5] + 'M'
            new_node.aircraft = self.aircraft_to_capacity(split1[5].strip())
            # Create a node and add it to our node list
            nodeList.append(Node(new_node.airline, new_node.start, new_node.end, new_node.departure, new_node.arrival, new_node.aircraft))
        f.close()
        return nodeList


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
    # List of flight nodes
    flight_list = graphMNG.read_input_file()
    # List of valid flights (end at JFK)
    valid_flights = graphMNG.valid_flight(flight_list)
    exit(0)
