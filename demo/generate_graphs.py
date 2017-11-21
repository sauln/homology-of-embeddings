import networkx as nx
from graph_generator import sphere_graph

def write_graph(graph, typename):
    nx.write_edgelist(graph, f"graphs/{typename}.edgelist", data=False)


def write_circle():
    graph = nx.cycle_graph(100)
    write_graph(graph, "circle")

def write_sphere():
    graph = sphere_graph()
    write_graph(graph, "sphere")


if __name__ == "__main__":
    write_sphere()
