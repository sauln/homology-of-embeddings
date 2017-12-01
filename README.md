# About

The goal of this project is to explore attributes of the Node2Vec graph embedding. This will be guided by the question "does Node2Vec preserve the homology of the graph?"

This is part of [Graph Theory Final Project](http://www.math.wsu.edu/courseinfo/syllabi/2017fall/m453-01-2173.pdf)

# Main experiment

1. Construct a random graph with known homology.
2. Embed the graph into a vector space via Node2Vec.
3. Compute persistent homology of the embedding.
4. Compare original homology to persistent homology.

# Questions

**Dimensionality**:

- Will persistent homology function in such high dimension?
  - No. Computing persistent homology of order 2 or higher is completely prohibitive.
- Does the dimensions of embedding effect whether homology is preserved?

**Accuracy**:

- How can you compare known homology to persistent homology?
- Is there a simple p-value or statistical test?

# Setup

We use [SNAP](https://snap.stanford.edu/snap/) node2vec implementation, [NetworkX](https://networkx.github.io/) for generating graphs, [Bokeh](https://bokeh.pydata.org/en/latest/) for plotting, and [UMAP](https://github.com/lmcinnes/umap) for dimensionality reduction. We use [Ripser](https://github.com/sauln/ripser) for computing persistent homology, but have made many modifications to the IO. Please use my fork <https://github.com/sauln/ripser>

After pointing the

```
chmod a+x generate_barcodes.sh
./run_example.sh
```

# Results

Preliminary experiments using a simple circle graph show that the persistent homology of produces expected results.
