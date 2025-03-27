import networkx as nx

g = nx.read_graphml("peel-A.graphml")
print(g.nodes(data=True))
print(len(g.nodes()))