import networkx as nx
from networkx.drawing import layout
import matplotlib.pyplot as plt

def plot_biclique(G, biclique=None):

    G1 = nx.Graph()
    G1.add_edges_from(G)
    pos = nx.bipartite_layout(G1, [u for u, v in G])
    #pos = nx.spring_layout(G1)
    #pos = layout.kamada_kawai_layout(G1)
    #layout.bipartite_layout(G1, [u for u, v in G])

    if biclique is not None:
        nx.draw_networkx_nodes(G1, pos, nodelist=biclique[0], node_color='green')
        nx.draw_networkx_nodes(G1, pos, nodelist=biclique[1], node_color='blue')
        nx.draw_networkx_nodes(G1, pos, nodelist=[node for node in G1 if node not in biclique[0]+biclique[1]], node_color='red')
        nx.draw_networkx_edges(G1, pos)
        nx.draw_networkx_labels(G1, pos)
    else:
        nx.draw(G1, pos, with_labels=True)





