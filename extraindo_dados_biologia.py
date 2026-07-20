import networkx as nx
import matplotlib.pyplot as plt

g = nx.DiGraph([
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
g.add_node("Bioética")
g.add_node("BECN")
g.add_node("BECM")
g.add_node("EDS")
g.add_node("CTS")

g_transitiva = nx.transitive_closure(g)

ordem = g.number_of_nodes()
ordem_denso = g_transitiva.number_of_nodes() 
tamanho = g.number_of_edges()
tamanho_denso = g_transitiva.number_of_edges()
densidade = nx.density(g)
densidade_denso = nx.density(g_transitiva)
assortatividade = nx.degree_assortativity_coefficient(g)
assortatividade_denso = nx.degree_assortativity_coefficient(g_transitiva)

centralidade = nx.betweenness_centrality(g)
vertice_maior_centralidade = max(centralidade, key=centralidade.get)

centralidade_denso = nx.betweenness_centrality(g_transitiva)
vertice_maior_centralidade_denso = max(centralidade_denso, key=centralidade_denso.get)

grau_saida = dict(g_transitiva.out_degree())
vertice_maior_saida= max(grau_saida, key=grau_saida.get)

grau_saida_denso = dict(g_transitiva.out_degree())
vertice_maior_saida_denso = max(grau_saida_denso, key=grau_saida_denso.get)

grau_entrada = dict(g_transitiva.in_degree())
vertice_maior_entrada = max(grau_entrada, key=grau_entrada.get)

grau_entrada_denso = dict(g_transitiva.in_degree())
vertice_maior_entrada_denso = max(grau_entrada_denso, key=grau_entrada_denso.get)

print(f"A ordem do grafo simplificado é: {ordem}")
print(f"A ordem do grafo denso é: {ordem_denso}")
print(f"O tamanho do grafo simplificado é: {tamanho}")
print(f"O tamanho do grafo denso é: {tamanho_denso}")
print(f"A densidade do grafo simplificado é: {densidade}")
print(f"A densidade do grafo denso é: {densidade_denso}")
print(f"A assortatividade do grafo simplificado é: {assortatividade}")
print(f"A assortatividade do grafo denso é: {assortatividade_denso}")

print(f"O vértice com maior centralidade no grafo denso é: {vertice_maior_centralidade_denso}")
print(f"O vértice com maior centralidade no grafo simplificado é: {vertice_maior_centralidade}")
print(f"O vértice com maior grau de saída no grafo simplificado é: {vertice_maior_saida}")
print(f"O vértice com maior grau de saída no grafo denso é: {vertice_maior_saida_denso}")
print(f"O vértice com maior grau de entrada no grafo simplificado é: {vertice_maior_entrada}")
print(f"O vértice com maior grau de entrada no grafo denso é: {vertice_maior_entrada_denso}")