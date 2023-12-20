import networkx as nx
import matplotlib.pyplot as plt


# Load the graph from a file
def load_graph(file_path):
    G = nx.DiGraph()
    with open(file_path, 'r') as file:
        for line in file:
            userA, userB = map(int, line.strip().split())
            G.add_edge(userA, userB)
    return G


# Define a function to compute degree histograms for directed graphs
def degree_histogram_directed(G, in_degree=False, out_degree=False):
    nodes = G.nodes()
    if in_degree:
        degseq = [d for n, d in G.in_degree()]
    elif out_degree:
        degseq = [d for n, d in G.out_degree()]
    else:
        degseq = [d for n, d in G.degree()]
    dmax = max(degseq) + 1
    freq = [0 for _ in range(dmax)]
    for d in degseq:
        freq[d] += 1
    return freq


# Load the graphs
medium_graph = load_graph('medium.in')
large_graph = load_graph('large.in')

# Question 3.1
print(f"Number of directed links (medium): {medium_graph.number_of_edges()}")
print(f"Number of directed links (large): {large_graph.number_of_edges()}")

# Question 3.2
print(f"Number of users (medium): {medium_graph.number_of_nodes()}")
print(f"Number of users (large): {large_graph.number_of_nodes()}")

# Question 3.3
in_degree_freq_medium = degree_histogram_directed(medium_graph, in_degree=True)
in_degree_freq_medium = [freq for freq in in_degree_freq_medium if freq > 0]
out_degree_freq_medium = degree_histogram_directed(medium_graph, out_degree=True)

in_degree_freq_large = degree_histogram_directed(large_graph, in_degree=True)
out_degree_freq_large = degree_histogram_directed(large_graph, out_degree=True)

# Plot degree distributions for medium graph
plt.figure(figsize=(12, 8))
plt.loglog(range(len(in_degree_freq_medium)), in_degree_freq_medium, 'go-', label='Medium In-degree', alpha=0.3)
plt.loglog(range(len(out_degree_freq_medium)), out_degree_freq_medium, 'bo-', label='Medium Out-degree', alpha=0.3)
plt.xlabel('Degree')
plt.ylabel('Frequency')
plt.legend()
plt.title('Degree Distribution (Medium Graph)')
plt.show()

# Plot degree distributions for large graph
plt.figure(figsize=(12, 8))
plt.loglog(range(len(in_degree_freq_large)), in_degree_freq_large, 'go-', label='Large In-degree', alpha=0.3)
plt.loglog(range(len(out_degree_freq_large)), out_degree_freq_large, 'bo-', label='Large Out-degree', alpha=0.3)
plt.xlabel('Degree')
plt.ylabel('Frequency')
plt.legend()
plt.title('Degree Distribution (Large Graph)')
plt.show()

# Question 3.4

print("Medium Network:")
weakly_connected_components = nx.number_weakly_connected_components(medium_graph)
print(f"Number of weakly connected components: {weakly_connected_components}")

# Number of strongly connected components
strongly_connected_components = nx.number_strongly_connected_components(medium_graph)
print(f"Number of strongly connected components: {strongly_connected_components}")

# Find the sizes of strongly connected components
strongly_connected_components_sizes = [len(component) for component in nx.strongly_connected_components(medium_graph)]

# Find the largest strongly connected component
largest_strongly_connected_component_size = max(strongly_connected_components_sizes)
print(f"Size of the largest strongly connected component: {largest_strongly_connected_component_size}")

# Alternatively, you can find the largest strongly connected component directly
largest_strongly_connected_component = max(nx.strongly_connected_components(medium_graph), key=len)
print(f"Nodes in the largest strongly connected component: {len(largest_strongly_connected_component)}")

# Number of nodes and links in the largest strongly connected component
num_nodes_largest_scc = len(largest_strongly_connected_component)
num_links_largest_scc = medium_graph.subgraph(largest_strongly_connected_component).number_of_edges()
print(f"Number of nodes in the largest strongly connected component: {num_nodes_largest_scc}")
print(f"Number of links in the largest strongly connected component: {num_links_largest_scc}")

print("Large Network:")
weakly_connected_components = nx.number_weakly_connected_components(large_graph)
print(f"Number of weakly connected components: {weakly_connected_components}")

# Number of strongly connected components
strongly_connected_components = nx.number_strongly_connected_components(large_graph)
print(f"Number of strongly connected components: {strongly_connected_components}")

# Find the sizes of strongly connected components
strongly_connected_components_sizes = [len(component) for component in nx.strongly_connected_components(large_graph)]

# Find the largest strongly connected component
largest_strongly_connected_component_size = max(strongly_connected_components_sizes)
print(f"Size of the largest strongly connected component: {largest_strongly_connected_component_size}")

# Alternatively, you can find the largest strongly connected component directly
largest_strongly_connected_component = max(nx.strongly_connected_components(large_graph), key=len)
print(f"Nodes in the largest strongly connected component: {len(largest_strongly_connected_component)}")

# Number of nodes and links in the largest strongly connected component
num_nodes_largest_scc = len(largest_strongly_connected_component)
num_links_largest_scc = large_graph.subgraph(largest_strongly_connected_component).number_of_edges()
print(f"Number of nodes in the largest strongly connected component: {num_nodes_largest_scc}")
print(f"Number of links in the largest strongly connected component: {num_links_largest_scc}")

# Question 3.5
#
# medium_average_clustering_coefficient = nx.average_clustering(medium_graph)
# large_average_clustering_coefficient = nx.average_clustering(large_graph)
#
# print(f"Average Clustering Coefficient for the mdeium network: {medium_average_clustering_coefficient}")
# print(f"Average Clustering Coefficient for the large network: {large_average_clustering_coefficient}")

# Question 3.6
largest_weakly_connected = max(nx.weakly_connected_components(medium_graph), key=len)

# Create a subgraph of the largest weakly connected component
largest_weakly_connected_subgraph = medium_graph.subgraph(largest_weakly_connected)

# Calculate the distance distribution
distances = nx.shortest_path_length(largest_weakly_connected_subgraph)
# Plot the distribution
pos = nx.spring_layout(largest_weakly_connected_subgraph)

# Set the figure size
plt.figure(figsize=(14, 10))

# Draw the nodes and edges
nx.draw(largest_weakly_connected_subgraph, pos, with_labels=False, node_color='lightblue', node_size=300, edge_color='grey')

# Draw the labels away from the nodes with a smaller font size
nx.draw_networkx_labels(largest_weakly_connected_subgraph, pos, font_size=8, font_color='black', font_family='sans-serif', alpha=0.7)

# Show the plot
plt.show()

# Question 3.7

# Calculate centrality measures
betweenness_centrality = nx.betweenness_centrality(medium_graph)
closeness_centrality = nx.closeness_centrality(medium_graph)
degree_centrality = nx.degree_centrality(medium_graph)

# Get the top 20 nodes for each centrality measure
top_betweenness_nodes = sorted(betweenness_centrality, key=betweenness_centrality.get, reverse=True)[:20]
top_closeness_nodes = sorted(closeness_centrality, key=closeness_centrality.get, reverse=True)[:20]
top_degree_nodes = sorted(degree_centrality, key=degree_centrality.get, reverse=True)[:20]

# Display the top nodes for each centrality measure
print("Top 20 Nodes by Betweenness Centrality:", top_betweenness_nodes)
print("Top 20 Nodes by Closeness Centrality:", top_closeness_nodes)
print("Top 20 Nodes by Degree Centrality:", top_degree_nodes)