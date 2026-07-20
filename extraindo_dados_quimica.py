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

g.add_nodes_from(["EDVT","BIOA","BECN","BECM","CTS","EDS"])

g_transitiva = nx.transitive_closure(g)

ordem = g.number_of_nodes()
ordem_denso = g_transitiva.number_of_nodes() 
tamanho = g.number_of_edges()
tamanho_denso = g_transitiva.number_of_edges()
densidade = nx.density(g)
densidade_denso = nx.density(g_transitiva)
r = nx.degree_assortativity_coefficient(g)
r_denso = nx.degree_assortativity_coefficient(g_transitiva)

centralidade_de_intermediacao = nx.betweenness_centrality(g)
vertice_maior_centralidade = max(centralidade_de_intermediacao, key=centralidade_de_intermediacao.get)

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
print(f"O coeficiente de assortatividade do grafo simplificado é: {r}")
print(f"O coeficiente de assortatividade do grafo denso é: {r_denso}")

print(f"O vértice com maior centralidade de intermediacao no grafo simplificado é: {vertice_maior_centralidade}")
print(f"O vértice com maior centralidade de intermediacao no grafo denso é: {vertice_maior_centralidade_denso}")
print(f"O vértice com maior grau de saída no grafo simplificado é: {vertice_maior_saida}")
print(f"O vértice com maior grau de saída no grafo denso é: {vertice_maior_saida_denso}")
print(f"O vértice com maior grau de entrada no grafo simplificado é: {vertice_maior_entrada}")
print(f"O vértice com maior grau de entrada no grafo denso é: {vertice_maior_entrada_denso}")