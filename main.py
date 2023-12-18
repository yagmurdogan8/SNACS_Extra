import networkx as nx
import matplotlib.pyplot as plt


# Load the graph from a file
def load_graph(file_path):
    G = nx.DiGraph()
    with open(file_path, 'r') as file:
        for line in file:
            userA, userB = map(int, line.strip().split('\t'))
            G.add_edge(userA, userB)
    return G


# Load the graphs
medium_graph = load_graph('medium.in')
large_graph = load_graph('large.in')

# Question 3.1
print(f"3.1 Number of directed links (medium): {medium_graph.number_of_edges()}")
print(f"3.1 Number of directed links (large): {large_graph.number_of_edges()}")

# Question 3.2
print(f"3.2 Number of users (medium): {medium_graph.number_of_nodes()}")
print(f"3.2 Number of users (large): {large_graph.number_of_nodes()}")

# Question 3.3
indegree_dist_medium = [in_degree for _, in_degree in medium_graph.in_degree]
outdegree_dist_medium = [out_degree for _, out_degree in medium_graph.out_degree]

# Plot indegree distribution
plt.hist(indegree_dist_medium, bins=50, alpha=0.5, label='Indegree')
plt.hist(outdegree_dist_medium, bins=50, alpha=0.5, label='Outdegree')
plt.xlabel('Degree')
plt.ylabel('Frequency')
plt.title('Indegree and Outdegree Distribution (medium)')
plt.legend()
plt.show()

# Repeat similar steps for large graph

# Continue with similar approaches for other questions.
