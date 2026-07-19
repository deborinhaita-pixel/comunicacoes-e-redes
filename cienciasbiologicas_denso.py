#Grafo Biologia

import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

G.add_edges_from([
    #BC&T
    ("BM","FUV"),
    ("FUV","FVV"),
    ("FUV","FEMEC"),
    ("BM","GA"),
    ("GA","FVV"),
    ("FVV","IEDO"),
    ("GA","FEMEC"),
    ("EM","TQ"),
    ("TQ","BQ"),
    ("EM","FETERM"),
    ("FEMEC", "FETERM"),
    ("BCC","NI"),
    ("PI","CR"),
    ("IEDO","FEMAG"),
    ("FEMEC","FEMAG"),
    ("FETERM","FQ"),
    ("FEMAG","FQ"),
    ("FUV", "IPE"),
    ("BCC", "PI"),

    #Matérias q saem de TQ
    ("TQ", "BQ"),
    ("BQ", "BioF"),
    ("BioF", "MicroB"),

    #Matérias q saem de EDVT
    ("EDVT", "GeoP"),
    ("EDVT", "SB"),
    ("EDP1", "EDP2"),
    ("EDP2", "FV1"),
    ("FV1", "FV2"),
    ("EDVT", "BioC"),

    #Matérias que saem de SB
    ("SB", "EDP1"),
    ("SB", "Evol"),
    ("SB", "ZODM"),
    ("ZODM", "ZE"),
    ("ZE", "ZV"),
    ("ZV", "MAC"),

    #Matérias que saem de BIOA
    ("BIOA", "EcoV"),
    ("BIOA", "EcoC"),
    ("BIOA", "PE"),
    ("BIOA", "MicroB"),

    #Matérias que saem de BioC
    ("BioC", "Gen1"),
    ("Gen1", "Gen2"),
    ("Gen2", "FV2"),
    ("Gen2", "Evol"),
    ("BioC", "BioF"),
    ("BioC", "FI"),
    ("BioC", "HE"),

    ("HE", "MH1"),
    ("MH1", "MH2"),
    ("MH1", "MH3"),

    ("Evol", "MAC"),
    ("IPE", "Evol"),


])

#Vértices sem ligação
G.add_node("Bioética")
G.add_node("BECN")
G.add_node("BECM")
G.add_node("EDS")
G.add_node("CTS")

G_transitive = nx.transitive_closure(G)

# Plotar o novo grafo
plt.figure(figsize=(20, 15))

# Usar um layout que espalha melhor os nós
pos = nx.spring_layout(G_transitive, k=0.5, seed=42)

nx.draw_networkx(
    G_transitive,
    pos,
    with_labels=True,
    node_color='lightpink',
    node_size=800,
    font_size=8,
    arrows=True,
    arrowsize=15,
    edge_color='black',
    alpha=0.5
)

nos_bct = ["BM","FUV","FVV","FEMEC","GA","FVV","IEDO","EM","TQ","BQ","FETERM","BCC","NI","PI","CR","IEDO","FEMAG","FQ","IPE","BECN","BECM","CTS","EDS"]
nx.draw_networkx_nodes(G_transitive, pos, nodelist=nos_bct, node_color="yellow", node_size=800, alpha=0.5) #pinta por cima

plt.title("Grafo denso de disciplinas do curso de Ciências Biológicas", fontsize=16)
plt.margins(0.1)
plt.show()