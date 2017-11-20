# About

The goal of this project is to explore the Node2Vec graph embedding.

To do this, we will ask the question "Does Node2Vec preserve the homology of the graph?"

# Main experiment

1. Construct a random graph with known homology.
  1. ensure correct format for node2vec input
2. Embed into a vector space via Node2Vec.
3. Compute persistent homology of the embedding.
4. Compare original homology to persistent homology.

# Expected hangups

**Dimensionality**: Embeddings are usually to high dimension ~300.

- Will persistent homology function in such high dimension?
- Does the dimensions of embedding effect whether homology is preserved?

**Accuracy**: I do not know how to compare known homology to persistent homology.

- How do we say how close the homology is?
- When does the preservation break down?
- Are new homology features created?

# Steps

Install snap 4.0

## Example node2vec

``` bash
cd ~/Downloads/Snap-4.0/examples/node2vec
./node2vec -i:graph/karate.edgelist -o:emb/karate.emb -l:3 -d:24 -p:0.3 -dr -v

```
