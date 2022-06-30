import os
import pyphi
import numpy as np

pyphi.config.load_file('../pyphi_config.yml')

tpm = np.array([[0,0,0],
                [0,1,1],
                [1,0,1],
                [1,1,1],
                [1,1,0],
                [1,1,1],
                [1,1,1],
                [1,1,1]])

cm = np.array([[0,1,1],[1,0,1],[1,1,1]])
node_labels = ('A', 'B', 'C')
network = pyphi.Network(tpm, cm=cm,node_labels=node_labels)
state = (0,0,0)
node_indices = (0, 1, 2)
subsystem = pyphi.Subsystem(network, state, node_labels)
A,B,C = subsystem.node_indices
print(subsystem.state)
mechanism = (A,B,C)
purview = (A,B,C)
cr = subsystem.cause_repertoire(mechanism, purview)
print(cr)
#print(cr[(0,0,0)])
flat_cr = pyphi.distribution.flatten(cr)
print(flat_cr)
mip = subsystem.effect_mip(mechanism, purview)
print("")
print("MIP")
print(mip)
sia = pyphi.compute.sia(subsystem)
print("MIP: \n", sia.cut)
print("Phi: \n Φ = ", sia.phi)
print("Time: \n", sia.time, "s")