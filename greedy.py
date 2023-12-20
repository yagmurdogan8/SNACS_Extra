import networkx as nx


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

densest_subgraph = greedy_densest_subgraph(your_graph)

# Print the nodes of the densest subgraph
print("Nodes in the Densest Subgraph:", densest_subgraph.nodes())

# Print the edges of the densest subgraph
print("Edges in the Densest Subgraph:", densest_subgraph.edges())
