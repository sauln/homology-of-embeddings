import click
import umap
import matplotlib.pyplot as plt

from sklearn import datasets
from utils import read_emb

@click.command()
@click.argument('filename', default="embeddings/karate.emb")
def plot_embedding(filename):
    data = read_emb(filename)

    if data.shape[1] > 2:
        print("Reduce dimensions")
        data = umap.UMAP().fit_transform(data)

    # Plot the dots at positions (x,y) = umap value
    plt.scatter(data[:,0], data[:,1])
    plt.show()

def plot_barcode():
    pass


if __name__ == "__main__":
    plot_embedding()
