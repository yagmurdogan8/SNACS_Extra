import networkx as nx
import matplotlib.pyplot as plt

undirected_graph = nx.Graph()

nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'H', 'I', 'J', 'K', 'L']
edges = [('A', 'D'), ('A', 'E'), ('A', 'B'), ('B', 'E'), ('B', 'F'), ('B', 'C'),
         ('C', 'F'), ('E', 'F'), ('E', 'I'), ('E', 'J'), ('F', 'J'), ('F', 'K'),
         ('F', 'H'), ('J', 'K'), ('L', 'K'), ('K', 'H')]
undirected_graph.add_nodes_from(nodes)
undirected_graph.add_edges_from(edges)
node_positions = {'A': (1, 2), 'B': (3, 2), 'C': (5, 2), 'D': (0, 1),
                  'E': (2, 1), 'F': (4, 1), 'H': (6, 1),
                  'I': (1, 0), 'J': (3, 0), 'K': (5, 0), 'L': (7, 0)}
nx.draw(undirected_graph, pos=node_positions, with_labels=True, node_size=500, font_size=10, font_color='black', font_weight='bold')
plt.title('Undirected graph for greedy')
plt.show()


def greedy_densest_subgraph(graph):
    densest_subgraphs = [graph.copy()]  # List to store graphs at each iteration
    current_density = nx.density(graph)

    while True:
        min_degree_node = min(graph, key=graph.degree)
        graph.remove_node(min_degree_node)
        new_density = nx.density(graph)

        if new_density > current_density:
            current_density = new_density
            densest_subgraphs.append(graph.copy())
            print(f"Iteration: Density = {current_density:.4f}, Nodes: {graph.nodes()}, Edges: {graph.edges()}")
        else:
            break

    return densest_subgraphs


densest_subgraphs = greedy_densest_subgraph(undirected_graph)

# iterations graphs (for all iteration the new graph)
for i, graph in enumerate(densest_subgraphs):
    plt.figure(figsize=(8, 6))
    nx.draw(graph, pos=node_positions, with_labels=True, node_size=500, font_size=10, font_color='black', font_weight='bold')
    plt.title(f'Iteration {i + 1}')
    plt.show()

# Print the nodes and edges of the densest subgraph
print("Nodes in the Densest Subgraph:", densest_subgraphs[-1].nodes())
print("Edges in the Densest Subgraph:", densest_subgraphs[-1].edges())
