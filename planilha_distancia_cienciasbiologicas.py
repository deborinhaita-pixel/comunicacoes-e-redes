#Grafo Biologia

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
G.add_node("Bioética")
G.add_node("BECN")
G.add_node("BECM")
G.add_node("EDS")
G.add_node("CTS")

import csv

# Defina a lista das suas matérias do BC&T
materias_bct = ['BM', 'FUV', 'GA', 'FVV', 'IEDO', 'FEMEC', 'FETERM', 'FEMAG', 'EM', 'TQ', 'BCC', 'PI', 'NI', 'CR', 'FQ', 'EDVT',
                'BIOA', 'BECN', 'BECM', 'CTS', 'EDS', 'IPE', 'BQ']

outras_materias = [n for n in G.nodes() if n not in materias_bct]

# Cria o arquivo CSV
with open('distancias_cienciasbiologicas_bct.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    
    # Escreve o cabeçalho
    writer.writerow(['BC&T'] + outras_materias)
    
    # Escreve as linhas
    for bct_node in materias_bct:
        if bct_node in G:
            linha = [bct_node]
            for target in outras_materias:
                try:
                    dist = nx.shortest_path_length(G, source=bct_node, target=target)
                    linha.append(dist)
                except nx.NetworkXNoPath:
                    linha.append('0')
            writer.writerow(linha)

print("Arquivo 'distancias_cienciasbiologicas_bct.csv' criado com sucesso na pasta do seu projeto!")