import numpy as np
import networkx
import matplotlib.pyplot as plt

from generate_graphs import sphere_graph, sphere, points_to_graph


def plot_sphere():
    """generate 1-sphere graph for paper """

    points = sphere(50, 2, 0)
    graph = points_to_graph(points, 10)

    positions = {i: p for i, p in enumerate(points)}
    networkx.draw(graph, pos=positions, node_size=20)
    plt.show()


def plot_random():
    points = np.random.randn(50,2)
    graph = points_to_graph(points, 15)

    positions = {i: p for i, p in enumerate(points)}
    networkx.draw(graph, pos=positions, node_size=20)
    plt.show()


if __name__ == "__main__":

    plot_sphere()
    plot_random()
