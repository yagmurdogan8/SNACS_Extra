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
    densest_subgraph = graph.copy()
    current_density = nx.density(densest_subgraph)

    while True:
        min_degree_node = min(densest_subgraph, key=densest_subgraph.degree)
        densest_subgraph.remove_node(min_degree_node)
        new_density = nx.density(densest_subgraph)

        if new_density > current_density:
            current_density = new_density
        else:
            break

    return densest_subgraph


densest_subgraph = greedy_densest_subgraph(undirected_graph)

# Print the nodes of the densest subgraph
print("Nodes in the Densest Subgraph:", densest_subgraph.nodes())

# Print the edges of the densest subgraph
print("Edges in the Densest Subgraph:", densest_subgraph.edges())
