#%%
#import library
import networkx as nx
import matplotlib.pyplot as plt
from pyvis.network import Network
from networkx.algorithms import community
# %%

G = nx.Graph();

G.add_edges_from([("نوید","b"),("c","b"),("0","2"),("0","نوید")])


print()
atter = dict(G.degree)



G["نوید"]['b']['weight'] =atter.get("a")
G["نوید"]['b']['weight'] =atter.get("a")

 
nx.set_node_attributes(G,atter,"with")
nx.set_node_attributes(G,atter,"size")
nx.set_node_attributes(G,atter,"value")
betweenses = nx.closeness_centrality(G)
print(betweenses)


# %%
G = nx.tutte_graph()
nx.draw(G)
print(nx.clustering(G))
print(nx.average_shortest_path_length(G))

plt.show()
net = Network(notebook=True,width='1000px',height='720px',bgcolor='#222222',font_color='white',directed=False)
net.from_nx(G)
net.show('test.html')
# %%
communities = list(community.greedy_modularity_communities(G))
print(communities)