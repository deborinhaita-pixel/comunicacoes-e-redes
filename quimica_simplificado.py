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

#Ajusta o tamanho da tela
plt.figure(figsize=(20, 15))

#Usar um layout que espalha melhor os nós
pos = nx.spring_layout(g, k=1.5, iterations=100)

nx.draw_networkx(
    g,
    pos,
    with_labels=True,
    node_color='lightgreen',
    node_size=800,
    font_size=8,
    arrows=True,
    arrowsize=15,
    edge_color='gray',
    alpha=0.5
)

plt.title("Grafo de disciplinas do curso de Química", fontsize=16)
plt.margins(0.1)
plt.show()