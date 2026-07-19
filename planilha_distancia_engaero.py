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

g.add_nodes_from(["EDVT", "BIOA","BECN","BECM","CTS","EDS","IE","PADM","DUTA", "SDE", "INOVA"]) #adiciona os vértices isolados

import csv

# Defina a lista das suas matérias do BC&T
materias_bct = ['BM', 'FUV', 'GA', 'FVV', 'IEDO', 'FEMEC', 'FETERM', 'FEMAG', 'EM', 'TQ', 'BCC', 'PI', 'NI', 'CR', 'FQ', 'EDVT',
                'BIOA', 'BECN', 'BECM', 'CTS', 'EDS', 'IPE', 'BQ']

outras_materias = [n for n in g.nodes() if n not in materias_bct]

# Cria o arquivo CSV
with open('distancias_engenhariaaeroespacial_bct.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    
    # Escreve o cabeçalho
    writer.writerow(['BC&T'] + outras_materias)
    
    # Escreve as linhas
    for bct_node in materias_bct:
        if bct_node in g:
            linha = [bct_node]
            for target in outras_materias:
                try:
                    dist = nx.shortest_path_length(g, source=bct_node, target=target)
                    linha.append(dist)
                except nx.NetworkXNoPath:
                    linha.append('0')
            writer.writerow(linha)

print("Arquivo 'distancias_engenhariaaeroespacial_bct.csv' criado com sucesso na pasta do seu projeto!")