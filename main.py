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
plt.loglog(range(len(in_degree_freq_medium)), in_degree_freq_medium, 'go-', label='Medium In-degree')
plt.loglog(range(len(out_degree_freq_medium)), out_degree_freq_medium, 'bo-', label='Medium Out-degree')
plt.xlabel('Degree')
plt.ylabel('Frequency')
plt.legend()
plt.title('Degree Distribution (Medium Graph)')
plt.show()

# Plot degree distributions for large graph
plt.figure(figsize=(12, 8))
plt.loglog(range(len(in_degree_freq_large)), in_degree_freq_large, 'go-', label='Large In-degree')
plt.loglog(range(len(out_degree_freq_large)), out_degree_freq_large, 'bo-', label='Large Out-degree')
plt.xlabel('Degree')
plt.ylabel('Frequency')
plt.legend()
plt.title('Degree Distribution (Large Graph)')
plt.show()
