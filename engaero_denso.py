#Grafo Engenharia Aeroespacial

import networkx as nx
import matplotlib.pyplot as plt

#Cria o grafo direcionado com as arestas em pares

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

    ("GA","ALGELIN"),
    ("FVV","CVT"),
    ("FUV","CN"), ("PI","CN"),
    ("FEMAG","CEF"),
    ("FUV","EC"),
    ("FETERM","MECFLU I"), ("FVV", "MECFLU I"),
    ("FETERM", "TERMOAPLI I"),
    ("FEMEC","MECSOL I"), ("DTEC", "MECSOL I"),
    ("FEMEC", "DIN I"), ("CN", "DIN I"), ("IEDO", "DIN I"),
    ("FVV","TSSL"),
    ("MECFLU I", "DING"),
    ("GA", "IA"),
    ("FEMEC","DEAERO"), ("AERO I-A","DEAERO"),
    ("MP","AEMC"), ("MECSOL I","AEMC"),
    ("TSSL", "SISCON I"),
    ("FVV","TCASA"), ("TERMOAPLI I","TCASA"),
    ("TERMOAPLI I","COMB I"),
    ("SISCON I", "SISCON II"),
    ("MECSOL I", "TECAE"),
    ("ALGELIN", "VIB"), ("DIN I", "VIB"),
    ("DING", "AEROD I"),
    ("DIN I", "DCVE"), ("SISCON I", "DCVE"),
    ("DEAERO", "ECA"),
    ("TECAE", "MCAE"), ("VIB","MCAE"),
    ("AEROD I", "AEROELA"), ("MCAE", "AEROELA"),
    ("DCVE", "LABGNC"),
    ("TECAE", "PEEA I"),
    ("DING", "SP I")])

g.add_nodes_from(["EDVT", "BIOA","BECN","BECM","CTS","EDS","IE","PADM","DUTA", "SDE", "INOVA"]) #Adiciona os vértices isolados

g_transitive = nx.transitive_closure(g)

# Plotar o novo grafo
plt.figure(figsize=(20, 15))

# Usar um layout que espalha melhor os nós
pos = nx.spring_layout(g_transitive, k=0.5, seed=42)

nx.draw_networkx(
    g_transitive,
    pos,
    with_labels=True,
    node_color='lightblue',
    node_size=800,
    font_size=8,
    arrows=True,
    arrowsize=15,
    edge_color='gray',
    alpha=0.5
)

plt.title("Grafo denso de disciplinas do curso de Engenharia Aeroespacial", fontsize=16)
plt.margins(0.1)
plt.show()