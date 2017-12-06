
"""

I want to create a slim module that can generate topologically interesting
graphs and point clounds


generate randomly
    * n-sphere
    * torus
    * klien bottle

"""

import networkx as nx

import numpy as np
from sklearn.neighbors import kneighbors_graph


def unit_sphere(npoints=1000, ndim=3):
    vec = np.random.randn(ndim, npoints)
    vec /= np.linalg.norm(vec, axis=0)
    vec = vec.T
    return vec


def sphere(npoints=1000, ndim=3, center=0):
    if type(center) is not list:
        center = [center] * ndim
    else:
        assert len(center) == ndim

    points = unit_sphere(npoints, ndim)
    points += center

    return points


def sphere_graph(npoints=1000, ndim=3, center=0, nneighbors=15):
    """ Create a graph from randomly sampled points on a sphere by connecting
        nearest neighbors

    """

    points = sphere(npoints, ndim, center)
    graph = points_to_graph(points, nneighbors)

    return graph


def points_to_graph(points, nneighbors):
    adj = kneighbors_graph(
        points, nneighbors, mode='connectivity', include_self=True)
    graph = nx.from_scipy_sparse_matrix(adj)

    return graph

def join_graphs(graphA, graphB):
    new_graph = nx.union(graphA, graphB, rename=('G-','H-') )
    assert len(new_graph.nodes) == len(graphA.nodes) + len(graphB.nodes)

    return new_graph


def double_ring():
    points = sphere() + sphere(1)
    graph = points_to_graph(points)
    return graph


def seperate_rings():
    points = np.concatenate((sphere(), sphere(center=5)))
    graph = points_to_graph(points)
    return graph


def random_graph(npoints=1000, ndim=3):
    points = np.random.randn(npoints, ndim)
    graph = points_to_graph(points, 15)
    return graph


def write_graph(graph, typename):
    nx.write_edgelist(graph, f"data/graphs/{typename}.edgelist", data=False)


def write_random_points(filename, npoints=1000, ndim=3):
    points = np.random.randn(npoints, ndim)
    np.savetxt(filename, points, delimiter=" ")


if __name__ == "__main__":
    # TODO: generate many more types of graphs
    #       They need to have nontrivial 0th and 1st homology.
    #       ring, double ring. 2 rings, etc.

    # write_graph(nx.cycle_graph(1000), "circle")
    write_graph(sphere_graph(ndim=2), "sphere2")
    write_graph(sphere_graph(ndim=3), "sphere3")
    write_graph(join_graphs(sphere_graph(ndim=2), sphere_graph(ndim=2)), "sphere2-disjoint-sphere2")


    write_graph(random_graph(), "random-graph")
    write_graph(nx.fast_gnp_random_graph(300, 0.1), "erdos-renyi-300-0.1")
    write_graph(nx.fast_gnp_random_graph(300, 0.2), "erdos-renyi-300-0.2")
    write_graph(nx.fast_gnp_random_graph(300, 0.5), "erdos-renyi-300-0.5")
    write_random_points("data/embeddings/random-points-2d.emb", ndim=2)
    write_random_points("data/embeddings/random-points-3d.emb", ndim=3)
    write_random_points("data/embeddings/random-points-4d.emb", ndim=4)
    # write_graph(double_ring(), "double_ring")
    # write_graph(seperate_rings(), "seperate_rings")
