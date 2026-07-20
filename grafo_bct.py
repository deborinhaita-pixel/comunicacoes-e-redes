#Grafo BC&T

import networkx as nx
import matplotlib.pyplot as plt

g = nx.Graph()

g.add_weighted_edges_from([
    ("BC&T", "Eng. Aero.", 12), 
    ("BC&T", "Química", 11), 
    ("BC&T", "Biologia", 8), 
    ("BC&T", "Biotecnologia", 11)
])

plt.figure(figsize=(20, 15))

# calcula as posições dos nós
pos = nx.spring_layout(g, seed=42) 

nx.draw_networkx(
    g,
    pos=pos,
    with_labels=True,
    node_color="red",
    node_size=800,
    font_size=8,
    arrows=True,
    arrowsize=15,
    edge_color='black',
    alpha=0.5
)

#desenha os pesos nas arestas do grafo
edge_labels = nx.get_edge_attributes(g, 'weight')
nx.draw_networkx_edge_labels(
    g,
    pos=pos,
    edge_labels=edge_labels,
    font_size=10,
    font_color='black'
)

plt.title("Grafo da relação entre o BC&T e os cursos específicos estudados", fontsize=16)
plt.margins(0.1)
plt.savefig("Imagens/grafo_bct_.png", dpi=300, bbox_inches='tight')
plt.show()
