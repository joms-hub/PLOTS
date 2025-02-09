import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
import networkx as nx

# Load data
net_data = pd.read_csv("D:\\.school\\'24\\2nd Semester\\dANAL\\networks_assignment.csv").set_index("LABELS")
print(net_data.head())

# Define node groups
primary_nodes = net_data.index.tolist()
primary_edges = [(primary_nodes[i], primary_nodes[(i + 1) % len(primary_nodes)]) for i in range(len(primary_nodes))]

secondary_nodes = ['BIH', 'GEO', 'ISR', 'MNE', 'SRB', 'CHE', 'TUR', 'UKR', 'GBR', 'AUS', 'HKG', 'USA']
secondary_edges = [(label, node) for label, row in net_data.iterrows() for node in secondary_nodes if node in row and row[node] > 0]

tertiary_nodes = ['AUT', 'BEL', 'BGR', 'HRV', 'CZE', 'EST', 'FRA', 'DEU', 'GRC', 'HUN', 'IRL', 'ITA', 'LVA', 'LUX', 'NLD', 'PRT', 'ROU', 'SVK', 'SVN', 'ESP']
tertiary_edges = [(label, node) for label, row in net_data.iterrows() for node in tertiary_nodes if node in row and row[node] > 0]

# Create graph
G = nx.Graph()

# Add nodes and edges
G.add_nodes_from(primary_nodes)
G.add_edges_from(primary_edges)

G.add_nodes_from(secondary_nodes)
G.add_edges_from(secondary_edges)

G.add_nodes_from(tertiary_nodes)
G.add_edges_from(tertiary_edges)

# Compute positions
primary_pos = nx.circular_layout(primary_nodes)  # Arrange primary nodes in a circle

# Distribute secondary nodes in an outer ring
secondary_pos = {node: (np.cos(angle) * 2, np.sin(angle) * 2) 
                 for node, angle in zip(secondary_nodes, np.linspace(0, 2 * np.pi, len(secondary_nodes), endpoint=False))}

# Distribute tertiary nodes in an even larger ring
tertiary_pos = {node: (np.cos(angle) * 3, np.sin(angle) * 3) 
                for node, angle in zip(tertiary_nodes, np.linspace(0, 2 * np.pi, len(tertiary_nodes), endpoint=False))}

# Combine all positions
positions = {**primary_pos, **secondary_pos, **tertiary_pos}

# Plot the graph
plt.figure(figsize=(12, 10))

# Draw nodes and edges with clear separation
nx.draw_networkx_nodes(G, positions, nodelist=primary_nodes, node_color='darkblue', node_size=800, label='Primary Nodes')
nx.draw_networkx_edges(G, positions, edgelist=primary_edges, edge_color='darkblue', width=2)

nx.draw_networkx_nodes(G, positions, nodelist=secondary_nodes, node_color='forestgreen', node_size=600, label='Secondary Nodes')
nx.draw_networkx_edges(G, positions, edgelist=secondary_edges, edge_color='forestgreen', width=1.5, alpha=0.7)

nx.draw_networkx_nodes(G, positions, nodelist=tertiary_nodes, node_color='gold', node_size=500, label='Tertiary Nodes')
nx.draw_networkx_edges(G, positions, edgelist=tertiary_edges, edge_color='gold', width=1.2, alpha=0.7)

# Add labels
nx.draw_networkx_labels(G, positions, font_size=9, font_color='black', font_weight='bold')

# Final adjustments
plt.title("Network Plot", fontsize=14)
plt.axis('off')
plt.show()