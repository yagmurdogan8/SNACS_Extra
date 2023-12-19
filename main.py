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
indegree_values = list(dict(medium_graph.in_degree()).values())
outdegree_values = list(dict(medium_graph.out_degree()).values())

# Exclude nodes with zero degrees
indegrees = list(dict(medium_graph.in_degree()).values())
outdegrees = list(dict(medium_graph.out_degree()).values())

# Exclude nodes with zero degrees
indegrees = [degree for degree in indegrees if degree > 0]
outdegrees = [degree for degree in outdegrees if degree > 0]

# Plot in-degrees
plt.hist(indegrees, bins=range(min(indegrees), max(indegrees) + 2), alpha=0.5, label='Indegree')
plt.xlabel('Indegree')
plt.ylabel('Frequency')
plt.title('Indegree Distribution (medium)')
plt.legend()
plt.show()

# Plot out-degrees
plt.hist(outdegrees, bins=range(min(outdegrees), max(outdegrees) + 2), alpha=0.5, label='Outdegree')
plt.xlabel('Outdegree')
plt.ylabel('Frequency')
plt.title('Outdegree Distribution (medium)')
plt.legend()
plt.show()
# Repeat similar steps for large graph

# Continue with similar approaches for other questions.
