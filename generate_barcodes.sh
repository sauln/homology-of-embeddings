## set these variables to point towards your copies.

NODE2VEC=~/Downloads/Snap-4.0/examples/node2vec
RIPSER=~/research/libraries/ripser/ripser

##

GRAPHROOT="data/graphs"
BARCODEROOT="data/barcodes"
DIAGRAMROOT="data/diagrams"
EMBEDROOT="data/embeddings"
RIPSERROOT="data/barcodes/ripser"

TMPFILE="data/tmp"
TMPFILE2="data/tmp2"


embed_graph () {
  FILE=$1
  DIM=$2

  EMBEDFILE="$EMBEDROOT/${FILE%.*}.emb"
  GRAPHFILE="$GRAPHROOT/$FILE"

  echo ""
  echo "Embed $GRAPHFILE"


  # -l walk length
  # -d dimension
  # -p return hyperparameter
  # -r number of walks per source
  # -k context size for optimization
  # -e number of epochs in SGD
  # -q inout hyperparameter

  # -w   graph is weighted
  # -dr  graph is directed
  # -v verbose output

  echo "--- Run node2vec on graph"
  $NODE2VEC/node2vec -i:$GRAPHFILE -o:$TMPFILE  > /dev/null
  # convert to nicer format
  python src/parse_ripser.py trim $TMPFILE $EMBEDFILE >/dev/null
}


compute_barcode () {

  FILE=$1
  RIPSERFILE="$RIPSERROOT/${FILE%.*}.r"
  BARCODEFILE="$BARCODEROOT/${FILE%.*}.json"
  BARCODEIMG="$DIAGRAMROOT/${FILE%.*}.png"
  EMBEDFILE="$EMBEDROOT/${FILE%.*}.emb"

  echo ""
  echo "Process $EMBEDFILE"

  echo "--- Compute barcode of embedding"
  $RIPSER --format point-cloud --dim 1 $EMBEDFILE --output $RIPSERFILE >/dev/null

  # convert to json
  python src/parse_ripser.py parse $RIPSERFILE $BARCODEFILE >/dev/null

  python src/visualize.py diagram $BARCODEFILE $BARCODEIMG

}


echo "Generate data"
python src/generate_graphs.py

echo ""
echo "Embed all graphs:"
echo " `ls data/graphs`"
for F in `ls data/graphs`
do
  embed_graph $F 5
done

echo ""
echo ""
echo "Compute barcodes for all of `ls data/embeddings`"
for F in `ls data/embeddings`
do
  compute_barcode $F
done

python src/visualize.py panel data/barcodes/graph-complete-2disjoint.json panel.png

rm $TMPFILE
