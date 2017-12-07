import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

from generate_graphs import sphere_graph, sphere, points_to_graph


def plot_sphere():
    """generate 1-sphere graph for paper """

    points = sphere(50, 2, 0)
    graph = points_to_graph(points, 10)

    positions = {i: p for i, p in enumerate(points)}
    nx.draw(graph, pos=positions, node_size=20)


def plot_random():
    points = np.random.randn(50,2)
    graph = points_to_graph(points, 15)

    positions = {i: p for i, p in enumerate(points)}
    nx.draw(graph, pos=positions, node_size=20)


def plot_disjoint_cycles():
    graph = nx.disjoint_union(nx.cycle_graph(200), nx.cycle_graph(200))
    cc = list(nx.connected_components(graph))
    assert len(cc) == 2

    assert all(i[0] == "G" or i[0] == "H" for i in cc[0])
    assert all(i[0] == "G" or i[0] == "H" for i in cc[1])



if __name__ == "__main__":

    #plot_sphere()
    #plot_random()
    plot_disjoint_cycles()
    plt.show()
