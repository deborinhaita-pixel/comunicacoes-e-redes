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

import csv

# Defina a lista das suas matérias do BC&T
materias_bct = ['BM', 'FUV', 'GA', 'FVV', 'IEDO', 'FEMEC', 'FETERM', 'FEMAG', 'EM', 'TQ', 'BCC', 'PI', 'NI', 'CR', 'FQ', 'EDVT',
                'BIOA', 'BECN', 'BECM', 'CTS', 'EDS', 'IPE', 'BQ']

outras_materias = [n for n in g.nodes() if n not in materias_bct]

# Cria o arquivo CSV
with open('distancias_quimica_bct.csv', 'w', newline='', encoding='utf-8') as f:
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

print("Arquivo 'distancias_quimica_bct.csv' criado com sucesso na pasta do seu projeto!")