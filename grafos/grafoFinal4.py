import os
import pyphi
import numpy as np
import networkx as nx
pyphi.config.load_file('../pyphi_config.yml')

tpm = np.array([
[0, 0, 0, 0, 0, 0],
[0, 1, 1, 0, 0, 0],
[0, 0, 0, 0, 0, 0],
[0, 1, 1, 0, 0, 0],
[0, 0, 0, 0, 0, 0],
[0, 1, 1, 0, 0, 0],
[1, 0, 0, 0, 0, 0],
[1, 1, 1, 0, 0, 0],
[0, 1, 1, 0, 0, 1],
[0, 0, 1, 0, 0, 1],
[0, 1, 1, 0, 0, 1],
[0, 0, 1, 0, 0, 1],
[0, 1, 1, 0, 0, 1],
[0, 0, 1, 0, 0, 1],
[1, 1, 1, 0, 0, 1],
[1, 0, 1, 0, 0, 1],
[0, 0, 1, 0, 0, 1],
[0, 1, 1, 0, 0, 1],
[0, 0, 1, 0, 0, 1],
[0, 1, 1, 0, 0, 1],
[0, 0, 1, 0, 0, 1],
[0, 1, 1, 0, 0, 1],
[1, 0, 1, 0, 0, 1],
[1, 1, 1, 0, 0, 1],
[0, 1, 1, 0, 0, 0],
[0, 0, 1, 0, 0, 0],
[0, 1, 1, 0, 0, 0],
[0, 0, 1, 0, 0, 0],
[0, 1, 1, 0, 0, 0],
[0, 0, 1, 0, 0, 0],
[1, 1, 1, 0, 0, 0],
[1, 0, 1, 0, 0, 0],
[0, 0, 0, 0, 0, 0],
[0, 1, 1, 0, 0, 0],
[0, 0, 0, 0, 0, 0],
[0, 1, 1, 0, 0, 0],
[0, 0, 0, 0, 1, 0],
[0, 1, 1, 0, 1, 0],
[1, 0, 0, 1, 1, 0],
[1, 1, 1, 1, 1, 0],
[0, 1, 1, 0, 0, 1],
[0, 0, 1, 0, 0, 1],
[0, 1, 1, 0, 0, 1],
[0, 0, 1, 0, 0, 1],
[0, 1, 1, 0, 1, 1],
[0, 0, 1, 0, 1, 1],
[1, 1, 1, 1, 1, 1],
[1, 0, 1, 1, 1, 1],
[0, 0, 1, 0, 0, 1],
[0, 1, 1, 0, 0, 1],
[0, 0, 1, 0, 0, 1],
[0, 1, 1, 0, 0, 1],
[0, 0, 1, 0, 1, 1],
[0, 1, 1, 0, 1, 1],
[1, 0, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1],
[0, 1, 1, 0, 0, 0],
[0, 0, 1, 0, 0, 0],
[0, 1, 1, 0, 0, 0],
[0, 0, 1, 0, 0, 0],
[0, 1, 1, 0, 1, 0],
[0, 0, 1, 0, 1, 0],
[1, 1, 1, 1, 1, 0],
[1, 0, 1, 1, 1, 0],
])

node_labels = ('A', 'B', 'C','D','E','F')
network = pyphi.Network(tpm,node_labels=node_labels)
state = (0, 0, 0, 0, 0, 0)
subsystem = pyphi.Subsystem(network, state, node_labels)
A,B,C,D,E,F = subsystem.node_indices
mechanism = (A,B,C,D,E,F)
purview = (A,B,C,D,E,F)
cr = subsystem.cause_repertoire(mechanism, purview)
flat_cr = pyphi.distribution.flatten(cr)
#print(flat_cr)
mip = subsystem.effect_mip(mechanism, purview)
print(mip)
sia = pyphi.compute.sia(subsystem)
print("MIP: \n", sia.cut)
print("Phi: \n Φ = ", sia.phi)
print("Time: \n", sia.time, "s")

