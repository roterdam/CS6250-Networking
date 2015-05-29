# Assignment 3 for OMS6250
#
# This how you run the topology and have it execute the Bellman-Ford algorithm.
# Generically, it is run as follows:
#     python run_topo.py <topology_file>
# For instance, to run topo1 that we created, use the following:
#     python run_topo.py topo1
#
# Copyright 2015 Sean Donovan


import sys
from Node import *

if len(sys.argv) != 2:
    print "Syntax:"
    print "    python run_topo.py <topology_file>"    
    exit()


# Populate the topology
topo = Topology(sys.argv[1])

# Run the topology.
topo.run_topo()
