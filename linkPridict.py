#%%
import networkx as nx 
import matplotlib.pyplot as plt 
  
G = nx.Graph() 
G.add_edges_from([(1, 2), (1, 3), (1, 4), (3, 4), (4, 5)]) 
  

nx.draw_networkx(G, with_labels = True)
# %%
