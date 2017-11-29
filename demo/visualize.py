import click
import umap
import matplotlib.pyplot as plt

import json

from bokeh.plotting import figure, show
from bokeh.layouts import gridplot

from sklearn import datasets
from utils import read_emb

from parse_ripser import ripser_to_dict


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

@click.command()
@click.argument('filename', default="barcodes/circle.bc")
def plot_barcode(filename):
    data = ripser_to_dict(filename)
    # with open(filename) as json_data:
    #     data = json.load(json_data)

    plots = []
    for dim, value in data.items():
        bars = {}
        bars['xs'] = []
        bars['ys'] = []

        p = figure(plot_width=600, plot_height=300, title=f"Dimension {dim}")
        p.yaxis.visible = False

        for i, bar in enumerate(value):
            start, end = bar
            level = i

            bars['xs'].append([start, end])
            bars['ys'].append([level, level])


        p.multi_line(xs="xs", ys="ys", line_width=5, source=bars)
        plots.append(p)

    show(gridplot([plots]))



if __name__ == "__main__":
    plot_barcode()
