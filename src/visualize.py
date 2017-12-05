import json

import click
import umap
import matplotlib.pyplot as plt


from bokeh.plotting import figure, show
from bokeh.layouts import gridplot
from bokeh.io import export_png


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
    plt.scatter(data[:, 0], data[:, 1])
    plt.show()


@click.command()
@click.argument('barcode')
@click.argument('outimg')
def plot_barcode(barcode, outimg):
    #data = ripser_to_dict(barcode)
    with open(barcode) as json_data:
        data = json.load(json_data)

    plots = []
    for dim, value in data.items():


        longest = max(x for _, x in value) * 1.5
        #  assert bars[-1][1] == -1.0, "the last bar should be until infty"

        # Assume last par goes to infty. Replace with a plotable upper bound.
        if value[-1][1] == -1.0:
            value[-1][1] = longest

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

    #outfile =
    plot = gridplot([plots])
    export_png(plot, filename=outimg)



if __name__ == "__main__":
    plot_barcode()
