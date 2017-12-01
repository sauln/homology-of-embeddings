import numpy as np

def read_emb(filename="embeddings/karate.emb"):

    with open(filename, "rb") as f:
        lines=f.readlines()

        # expect first line has tuple (#nodes, #dimension)
        preamble = np.fromstring(lines[0], dtype=int, sep=' ')
        embedding = np.zeros(preamble)

        for line in lines[1:]:
            # first value of line ids the node
            arr = np.fromstring(line, dtype=float, sep=' ')
            idx, emb = int(arr[0]), arr[1:]

            # order embdding by index.
            embedding[idx,:] = emb

    return embedding
