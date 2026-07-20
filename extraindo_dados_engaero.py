import networkx as nx
import matplotlib.pyplot as plt

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

g.add_nodes_from(["EDVT", "BIOA","BECN","BECM","CTS","EDS","IE","PADM","DUTA", "SDE", "INOVA"])
g_transitiva = nx.transitive_closure(g)

ordem = g.number_of_nodes()
ordem_denso = g_transitiva.number_of_nodes() 
tamanho = g.number_of_edges()
tamanho_denso = g_transitiva.number_of_edges()
densidade = nx.density(g)
densidade_denso = nx.density(g_transitiva)
r = nx.degree_assortativity_coefficient(g)
r_denso = nx.degree_assortativity_coefficient(g_transitiva)

print(f"A ordem do grafo simplificado é: {ordem}")
print(f"A ordem do grafo denso é: {ordem_denso}")
print(f"O tamanho do grafo simplificado é: {tamanho}")
print(f"O tamanho do grafo denso é: {tamanho_denso}")
print(f"A densidade do grafo simplificado é: {densidade}")
print(f"A densidade do grafo denso é: {densidade_denso}")
print(f"O coeficiente de assortatividade do grafo simplificado é: {r}")
print(f"O coeficiente de assortatividade do grafo denso é: {r_denso}")
