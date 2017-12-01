
"""

I want to create a slim module that can generate topologically interesting
graphs and point clounds


generate randomly
    * n-sphere
    * torus
    * klien bottle

"""

import networkx

import numpy as np
from sklearn.neighbors import kneighbors_graph

def sphere(npoints=1000, ndim=3):
    vec = np.random.randn(ndim, npoints)
    vec /= np.linalg.norm(vec, axis=0)
    vec = vec.T
    return vec

def sphere_graph(npoints=1000, ndim=3, nneighbors=5):
    """ Create a graph from randomly sampled points on a sphere by connecting
        nearest neighbors

    """

    points = sphere(npoints, ndim)
    adj = kneighbors_graph(points, nneighbors, mode='connectivity', include_self=True)
    graph = networkx.from_scipy_sparse_matrix(adj)

    return graph


if __name__ == "__main__":
    sphere_graph(100)
