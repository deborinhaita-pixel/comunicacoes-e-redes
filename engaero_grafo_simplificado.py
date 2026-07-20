#Grafo Engenharia Aeroespacial
#me ame imediatamente 

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

g.add_nodes_from(["EDVT", "BIOA","BECN","BECM","CTS","EDS","IE","PADM","DUTA", "SDE", "INOVA"]) #adiciona os vértices isolados

nos_bct = ["BM","FUV","FVV","FEMEC","GA","FVV","IEDO","EM","TQ","BQ","FETERM","BCC","NI","PI","CR","IEDO","FEMAG","FQ","IPE","BECN","BECM","CTS","EDS"]

cor_dos_nos = []

for nodo in g.nodes():
    if nodo in nos_bct:
        cor_dos_nos.append("yellow")
    else:
        cor_dos_nos.append("lightblue")

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

plt.title("Grafo simplificado de disciplinas do curso de Engenharia Aeroespacial", fontsize=16)
plt.margins(0.1)
plt.savefig("Imagens/grafo_engaero_simplificado.png", dpi=300, bbox_inches='tight')
plt.show()