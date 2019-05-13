import networkx as nx
import pickle as pk
import pandas as pd
import numpy as np


types = { #type colors according to Pokemon games
        
        "grass"     : 0x78C850,
        "fire"      : 0xE24242,
        "water"     : 0x6890F0,
        "poison"    : 0xA040A0,
        "flying"    : 0xA890F0,
        "fighting"  : 0xC03028,
        "steel"     : 0xB8B8D0,
        "normal"    : 0xA8A878,
        "dark"      : 0x705848,
        "electric"  : 0xF8D030,
        "dragon"    : 0x7038F8,
        "psychic"   : 0xF85888,
        "bug"       : 0xA8B820,
        "fairy"     : 0xEE99AC,
        "rock"      : 0xB8A038,
        "ground"    : 0xE0C068,
        "ice"       : 0x98D8D8,
        "ghost"     : 0x705898
}

s = {} #will be used to determine the size of nodes
for t in types:
    s.update({t:0})

G = nx.Graph()


    
dex = pk.load(open("dex.p", "rb"))

df = pd.DataFrame(np.zeros([18,18], dtype=int))
df.columns = types.keys()
df.index = types.keys()

for entry in dex.values():
    for t in entry:
        s[t] += 1
    if(len(entry) > 1):
        df[entry[0]][entry[1]]+=1
        df[entry[1]][entry[0]]+=1

for t in types.items():
    G.add_node(t[0], color = t[1], size = s[t[0]])
        
for i,t1 in enumerate(types):
    for j,t2 in enumerate(types):
        if(j > i):
            G.add_edge(t1,t2, weight=int(df[t1][t2]))

G.remove_edges_from(G.selfloop_edges())
nx.write_graphml(G, "types.graphml")