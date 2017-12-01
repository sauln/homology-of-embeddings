## set these variables to point towards your copies.

NODE2VEC=~/Downloads/Snap-4.0/examples/node2vec
RIPSER=~/research/libraries/ripser/ripser

##

GRAPHROOT="data/graphs"
BARCODEROOT="data/barcodes"

TMPFILE="data/tmp"
TMPFILE2="data/tmp2"




#echo ""
#echo "Generate graphs"
#python generate_graphs.py

for FILE in `ls data/graphs`
do
  echo ""
  echo "Process $GRAPHROOT/$FILE"

  echo "--- Run node2vec graph"
  $NODE2VEC/node2vec -i:$GRAPHROOT/$FILE -o:$TMPFILE -l:20 -d:5 -p:1 -dr > /dev/null

  python src/parse_ripser.py trim $TMPFILE $TMPFILE >/dev/null

  echo "--- Compute barcode of embedding"
  $RIPSER --format point-cloud --dim 1 $TMPFILE --output $TMPFILE2 >/dev/null

  echo "--- Convert barcode to JSON"
  python src/parse_ripser.py parse $TMPFILE2 "$BARCODEROOT/${FILE%.*}.json" >/dev/null

  #python visualize.py $BARCODEFILE
done

rm $TMPFILE $TMPFILE2
