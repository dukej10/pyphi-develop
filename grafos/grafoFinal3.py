import os
import pyphi
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


pyphi.config.load_file('../pyphi_config.yml')

tpm = np.array([
    [0,0,0],
    [0,0,0],
    [1,0,0],
    [1,0,1],
    [0,1,0],
    [0,1,0],
    [1,1,0],
    [1,1,1]
])


cm = np.array([
     [0,1,1],
     [1,0,1],
     [1,1,0]
 ])


node_labels = ('A', 'B', 'C')
network = pyphi.Network(tpm,cm = cm,node_labels=node_labels)
state = (1, 1, 1)
subsystem = pyphi.Subsystem(network, state, node_labels)
A,B,C = subsystem.node_indices
mechanism = (A,B,C)
purview = (A,B,C)
cr = subsystem.cause_repertoire(mechanism, purview)
flat_cr = pyphi.distribution.flatten(cr)
# print(flat_cr)
mip = subsystem.effect_mip(mechanism, purview)
# print(mip)
sia = pyphi.compute.sia(subsystem)
#print("MIP: \n", sia.cut)
print(str(sia.cut))
nodes = list(node_labels)
lista = cm.tolist()
dictnode = {}
# print("Phi: \n Φ = ", sia.phi)
# print("Time: \n", sia.time, "s")
G = nx.Graph()
lista = list(node_labels)
dic = {}
aux = []
G.add_nodes_from(lista)
for i in range(0,len(lista)):
    for j in range(0, len(lista)):
        if cm[i][j] != 0:
            #print("ADYACENCIA ", cm[i][j] , " x ", lista[j])
            aux.append(lista[j])
    dic[lista[i]] = aux
    aux = []
print(dic)
# def show_graph_with_labels(adjacency_matrix, mylabels, accion):
#     rows, cols = np.where(adjacency_matrix == 1)
#     edges = zip(rows.tolist(), cols.tolist())
#     gr = nx.Graph()
#     if accion == "crear":
#         gr.add_edges_from(edges)
#         nx.draw(gr, node_size=500, labels=mylabels, with_labels = True)
#         plt.show()
#     if accion == "cortar":
#         gr.remove_edge(0,1)
#         nx.draw(gr, node_size=500, labels=mylabels, with_labels = True)
#         plt.show()



for i in range(0,len(nodes)):
    dictnode[i] = nodes[i]
# print(dictnode)
# labeldict = {}
# labeldict[0] = "A"
# labeldict[1] = "B"
# labeldict[2] = "C"

# show_graph_with_labels(cprueba, dictnode, "crear")

# G = nx.Graph()
# G.add_node("Kevin Bacon")
# G.add_node("Tom Hanks")
# nx.draw(G, node_size=500, with_labels = True)
# plt.show()