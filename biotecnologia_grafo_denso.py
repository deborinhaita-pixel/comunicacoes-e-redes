#Grafo de Biotecnologia

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


    #Matérias q saem de BQ
    ("BQ","IBioinf"),
    ("BQ","IBiotec"),
    ("BQ","BS"),
    ("BQ","BF"),
    ("BQ","PFB"),
    ("BQ","Farmac"),
    ("BQ","EngM"),
    ("BQ","TF"),

    #Matérias q saem de BMB
    ("BMB","EngM"),
    ("BMB","NanoB"),
    ("BMB","GPG"),
    ("BMB","EB"),
    ("BMB","BA"),
    ("BMB","BH"),
    ("BMB","PR"),
    ("PR","LB"),
    ("BMB","SRB"),
    ("HE","BMB"),

    #Matérias q saem de Farmac
    ("Farmac","SRB"),
    ("Farmac","NanoB"),
    ("Farmac","EB"),
    ("Farmac","LB"),

    #Matérias que saem de PI
    ("PI", "CN"),
    ("FUV", "CN"),
    ("CN", "CCAPB"),
    ("IPE", "CCAPB"),
    ("CCAPB","Bioest"),

    #Matérias que saem de BioC
    ("BioC", "BF"),
    ("BioC", "HE"),
    ("BioC", "G1"),
    ("BioC", "IBioinf"),
    ("BioC", "FI"),

    ("G1", "G2"),
    ("G1", "PFB"),

    ("G2", "BS"),
    ("G2", "FV2"),
    ("FV2", "BV"),
    ("G2", "LB"),
    ("G2", "EB"),
    ("G2", "NanoB"),

    ("BF", "Microb"),
    ("Microb", "PR"),

    ("FI", "BH"),

    #Matérias q saem de EDVT

    ("EDVT", "SB"),
    ("SB", "EDP1"),
    ("EDP1", "EDP2"),
    ("EDP2", "FV1"),
    ("FV1", "FV2"),
    ("EDVT", "BIOA"),
    ("EDVT", "BioC"),

    ("BIOA", "IBiotec"),
    ("IBiotec", "EPPB"),




])

#Vértices sem ligação
G.add_node("Bioética")
G.add_node("FB")
G.add_node("BECM")
G.add_node("BECN")
G.add_node("EDS")
G.add_node("CTS")

G_transitiva = nx.transitive_closure(G)

nos_bct = ["BM","FUV","FVV","FEMEC","GA","IEDO","EM","TQ","BQ","FETERM","BCC","NI","PI","CR","FEMAG","FQ","IPE","BECN","BECM","CTS","EDS","BIOA","EDVT"]

cor_dos_nos = []

for nodo in G_transitiva.nodes():
    if nodo in nos_bct:
        cor_dos_nos.append("yellow")
    else:
        cor_dos_nos.append("purple")

# Plotar o novo grafo
plt.figure(figsize=(20, 15))

# Usar um layout que espalha melhor os nós
pos = nx.spring_layout(G_transitiva, k=0.5, seed=42)

nx.draw_networkx(
    G_transitiva,
    pos,
    with_labels=True,
    node_color=cor_dos_nos,
    node_size=800,
    font_size=8,
    arrows=True,
    arrowsize=15,
    edge_color='black',
    alpha=0.5
)

plt.title("Grafo denso de disciplinas do curso de Biotecnologia", fontsize=16)
plt.margins(0.1)
plt.savefig("Imagens/grafo_biotecnologia_denso.png", dpi=300, bbox_inches='tight')
plt.show()