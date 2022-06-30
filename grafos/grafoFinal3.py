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
corte = str(sia.cut)
cortes = corte.replace("Cut", "")
listaux = []
listver = []
alfabeto = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
for i in cortes:
    if i in alfabeto:
        listaux.append(i)
    if i == "]":
         listver.append(listaux)
         listaux = []
print(listver)
nodes = list(node_labels)
lista = cm.tolist()
dictnode = {}
##  -------------- GRAFO INICIAL ------
G = nx.Graph()
lista = list(node_labels)
dic = {}
aux = []
G.add_nodes_from(lista)
for i in range(0,len(lista)):
    for j in range(0, len(lista)):
        if cm[i][j] != 0:
            aux.append(lista[j])
    dic[lista[i]] = aux
    aux = []
for clave, valor in dic.items():
        for nodo in valor:
                G.add_edge(clave, nodo)
nx.draw(G, node_size=500, with_labels = True)
plt.show()
## -----------------------------------------------

## ----------------------- Grafo con corte ---------------
G2 = nx.Graph()
G2.add_nodes_from(lista)
for clave, valor in dic.items():
        for nodo in valor:
            if clave in listver[0]  and nodo in listver[0]:
                G2.add_edge(clave, nodo)
            elif clave in listver[1]  and nodo in listver[1]:
                G2.add_edge(clave, nodo)
nx.draw(G2, node_size=500, with_labels = True)
plt.show()



# for i in range(0,len(nodes)):
#     dictnode[i] = nodes[i]
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