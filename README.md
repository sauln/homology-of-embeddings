# About

The goal of this project is to explore attributes of the Node2Vec graph embedding. This will be guided by the question "does Node2Vec preserve the homology of the graph?"

This is part of [Graph Theory Final Project](http://www.math.wsu.edu/courseinfo/syllabi/2017fall/m453-01-2173.pdf)


# Main experiment

1. Construct a random graph with known homology.
2. Embed the graph into a vector space via Node2Vec.
3. Compute persistent homology of the embedding.
4. Compare original homology to persistent homology.

# Expected hangups

**Dimensionality**: Embeddings are usually to high dimension ~300.

- Will persistent homology function in such high dimension?
- Does the dimensions of embedding effect whether homology is preserved?

**Accuracy**: I do not know how to compare known homology to persistent homology.

# Setup

We use [SNAP](https://snap.stanford.edu/snap/) node2vec implementation, [Ripser](https://github.com/sauln/ripser) for computing persistent homology, [NetworkX](https://networkx.github.io/) for generating graphs, [Bokeh](https://bokeh.pydata.org/en/latest/) for plotting, and [UMAP](https://github.com/lmcinnes/umap) for dimensionality reduction.

```
cd demo
chmod a+x run_example.sh
./run_example.sh
```

# Results

Preliminary experiments using a simple circle graph show that the persistent homology of produces expected results.
