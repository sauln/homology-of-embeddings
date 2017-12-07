import json

import numpy as np

import click
import umap
import matplotlib.pyplot as plt


from bokeh.plotting import figure, show
from bokeh.layouts import gridplot
from bokeh.io import export_png

from sklearn import datasets
from utils import read_emb

from parse_ripser import ripser_to_dict


colors = {"0": "green", "1": "blue"}


def persistence_diagram(data):

    data, longest = fix_longest(data)
    buff = longest * 0.05

    p = figure(plot_width=600, plot_height=600, title=f"Persistence DiagramsX", y_range=(-buff,longest+buff), x_range=(-buff, longest+buff))

    #with data['0'] as dimdat:
    dimdat = data['0']
    for dim, dat in data.items():
        xs = [d[0] for d in dat]
        ys = [d[1] for d in dat]

        p.scatter(xs, ys, color=colors[dim], size=20)

    p.line(x=[0, longest], y=[0, longest], color="red")

    return p


def fix_longest(data):

    longest = max(max(x for _, x in value) for dim, value in data.items() ) * 1.3

    for dim, value in data.items():
        # Assume last par goes to infty. Replace with a plotable upper bound.
        if value[-1][1] == -1.0:
            value[-1][1] = longest

    return data, longest


def same_axes(data):

    longest = max(max(x for _, x in value) * 1.5 for dim, value in data.items() )

    print(longest)
    p = figure(plot_width=600, plot_height=600, title=f"Persistence DiagramsX", x_range=(0, longest))
    p.yaxis.visible = False

    colors = {"0": "red", "1": "blue"}

    bars = {}
    bars['xs'] = []
    bars['ys'] = []
    bars['color'] = []

    current = 0
    for dim, value in data.items():
        # Assume last par goes to infty. Replace with a plotable upper bound.
        if value[-1][1] == -1.0:
            value[-1][1] = longest

        # import pdb; pdb.set_trace()
        # bars['line_color'] = colors[dim]
        #import pdb; pdb.set_trace()
        for i, bar in enumerate(value):
            start, end = bar
            level = current+i

            bars['xs'].append([start, end])
            bars['ys'].append([level, level])
            bars['color'].append(colors[dim])

        current = level

    p.multi_line(xs="xs", ys="ys", line_width=5, source=bars)
    return p



def per_dimension(data):
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


    return plot



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
@click.argument('action')
@click.argument('barcode')
@click.argument('outimg')
def plot_persistence(action, barcode, outimg):
    with open(barcode) as json_data:
        data = json.load(json_data)

    if action == "diagram":
        plot = persistence_diagram(data)
    if action == "barcode":
        plot = per_dimension(data)
    if action == "broken":
        plot = same_axes(data)

    export_png(plot, filename=outimg)


if __name__ == "__main__":
    plot_persistence()
