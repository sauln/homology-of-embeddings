import json
from collections import defaultdict

import click
import numpy as np

from more_itertools import flatten
from utils import read_emb

def ripser_to_dict(infile):
    print("Convert ripser output into json")
    with open(infile, "rb") as f:
        lines = f.readlines()

    barcode = defaultdict(list)

    for line in lines:
        line = line.decode('utf-8')
        dim, start, end = line.split(" ")
        dim, start, end = float(dim), float(start), float(end)

        barcode[dim].append( [start, end] )

    for dim, bars in barcode.items():
        largest = max(e for _, e in bars)
        bars = [ [s,e] if e != -1 else [s, largest] for s,e in bars]
        barcode[dim] = bars

    return barcode


def parse_barcode(infile, outfile):
    """ This converts the command line output from Ripser into JSON format.
    """


    print("Convert ripser output into json")
    with open(infile, "rb") as f:
        lines = f.readlines()

    persistence_diagram = {}

    max_range = float(lines[2].decode('utf-8').split(",")[1].replace("]", ""))

    # find dim N start and finish
    for line in lines[3:]:
        line = line.decode('utf-8')
        if line.startswith("persistence"):
            current_diagram = line.replace("persistence intervals in ", "").replace(":\n", "")
            persistence_diagram[current_diagram] = []
        else:
            start, finish = line.split(",")
            start = float(start.replace(" [", ""))

            if finish[:2] == ' )':
                finish = max_range
            else:
                finish = float(finish.replace(")\n", ""))

            persistence_diagram[current_diagram].append([start, finish])

    with open(outfile, 'w') as fp:
        json.dump(persistence_diagram, fp)


def trim_ripser(infile, outfile):
    """ Convert the emb output from node2vec into a point-cloud
        so ripser can use it.
    """

    print("Convert point-cloud to trimmed format for ripser")
    emb = read_emb(infile)
    emb = emb[1:,]

    np.savetxt(outfile, emb, delimiter=" ")


@click.command()
@click.argument('action', default='parse')
@click.argument('infile', default="barcodes/circle.bc")
@click.argument('outfile', default="barcodes/circle_bc.json")
def execute_formatting(action, infile, outfile):
    if action == "trim":
        trim_ripser(infile, outfile)
    if action == "parse":
        parse_barcode(infile, outfile)


if __name__ == "__main__":
    #execute_formatting()
    ripser_to_dict("barcodes/sphere.bc")
