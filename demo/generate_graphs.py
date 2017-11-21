import networkx as nx


def write_graph(graph, typename):
    nx.write_edgelist(graph, f"graphs/{typename}.edgelist", data=False)


def write_circle():
    graph = nx.cycle_graph(100)
    write_graph(graph, "circle")


if __name__ == "__main__":
    write_circle()
