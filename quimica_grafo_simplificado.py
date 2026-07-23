#Grafo Química

import networkx as nx
import matplotlib.pyplot as plt

#Cria o grafo com as arestas em pares
g = nx.DiGraph([
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

    ("TQ","FUNDQ"),
    ("FETERM","PT"), ("FVV","PT"),
    ("TQ", "FRO"),
    ("FEMAG","EMA"), ("FUNDQ","EMA"),
    ("PT", "TERMOQ"), ("TQ", "TERMOQ"),
    ("TQ", "QAC I"),
    ("FRO", "MRO"),
    ("MRO", "MAQO"),
    ("MAQO", "QOE"),
    ("TQ", "CQ"), ("PT", "CQ"),
    ("EMA", "LQ"),
    ("QAC I", "QAC II"),
    ("LQ", "QE"),
    ("MRO", "TEQO"),
    ("QE", "QC"),
    ("QAC II", "ESPECMA"),
    ("PT", "ELETROQ"), ("TQ", "ELETROQ"),
    ("BQ", "QMB"), ("QAC II", "QMB"),
    ("ESPECMA", "EIQ"), ("ELETROQ", "EIQ"),
    ("TERMOQ", "FQEXP"),
    ("ESPECMA","TAS")
])

#Adiciona os nós soltos
g.add_nodes_from(["EDVT","BIOA","BECN","BECM","CTS","EDS"])

nos_bct = ["BM","FUV","FVV","FEMEC","GA","IEDO","EM","TQ","BQ","FETERM","BCC","NI","PI","CR","FEMAG","FQ","IPE","BECN","BECM","CTS","EDS","BIOA","EDVT"]
cor_dos_nos = []

for nodo in g.nodes():
    if nodo in nos_bct:
        cor_dos_nos.append("yellow")
    else:
        cor_dos_nos.append("lightgreen")

# Plotar o novo grafo
plt.figure(figsize=(20, 15))

# Usar um layout que espalha melhor os nós
pos = nx.spring_layout(g, k=0.5, seed=42)

nx.draw_networkx(
    g,
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

plt.title("Grafo simplificado de disciplinas do curso de Química", fontsize=16)
plt.margins(0.1)
plt.savefig("Imagens/grafo_quimica_simplificado.png", dpi=300, bbox_inches='tight')
plt.show()