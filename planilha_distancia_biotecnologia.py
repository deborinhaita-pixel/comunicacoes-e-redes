#Grafo de Biotecnologia

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

    #Matérias q saem de BQ
    ("BQ","IBioinf"),
    ("BQ","IBiotec"),
    ("BQ","BS"),
    ("BQ","BF"),
    ("BQ","PFB"),
    ("BQ","Farmac"),
    ("BQ","EngM"),
    ("BQ","TF"),

    #Matérias q saem de BMB
    ("BMB","EngM"),
    ("BMB","NanoB"),
    ("BMB","GPG"),
    ("BMB","EB"),
    ("BMB","BA"),
    ("BMB","BH"),
    ("BMB","PR"),
    ("PR","LB"),
    ("BMB","SRB"),
    ("HE","BMB"),

    #Matérias q saem de Farmac
    ("Farmac","SRB"),
    ("Farmac","NanoB"),
    ("Farmac","EB"),
    ("Farmac","LB"),

    #Matérias que saem de PI
    ("PI", "CN"),
    ("FUV", "CN"),
    ("CN", "CCAPB"),
    ("IPE", "CCAPB"),
    ("CCAPB","Bioest"),

    #Matérias que saem de BioC
    ("BioC", "BF"),
    ("BioC", "HE"),
    ("BioC", "G1"),
    ("BioC", "IBioinf"),
    ("BioC", "FI"),

    ("G1", "G2"),
    ("G1", "PFB"),

    ("G2", "BS"),
    ("G2", "FV2"),
    ("FV2", "BV"),
    ("G2", "LB"),
    ("G2", "EB"),
    ("G2", "NanoB"),

    ("BF", "Microb"),
    ("Microb", "PR"),

    ("FI", "BH"),

    #Matérias q saem de EDVT

    ("EDVT", "SB"),
    ("SB", "EDP1"),
    ("EDP1", "EDP2"),
    ("EDP2", "FV1"),
    ("FV1", "FV2"),
    ("EDVT", "BIOA"),
    ("EDVT", "BioC"),

    ("BIOA", "IBiotec"),
    ("IBiotec", "EPPB"),




])

#Vértices sem ligação
G.add_node("Bioética")
G.add_node("FB")
G.add_node("BECM")
G.add_node("BECN")
G.add_node("EDS")
G.add_node("CTS")

import csv

# Defina a lista das suas matérias do BC&T
materias_bct = ['BM', 'FUV', 'GA', 'FVV', 'IEDO', 'FEMEC', 'FETERM', 'FEMAG', 'EM', 'TQ', 'BCC', 'PI', 'NI', 'CR', 'FQ', 'EDVT',
                'BIOA', 'BECN', 'BECM', 'CTS', 'EDS', 'IPE', 'BQ']

outras_materias = [n for n in G.nodes() if n not in materias_bct]

# Cria o arquivo CSV
with open('distancias_biotecnologia_bct.csv', 'w', newline='', encoding='utf-8') as f:
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

print("Arquivo 'distancias_biotecnologia_bct.csv' criado com sucesso na pasta do seu projeto!")