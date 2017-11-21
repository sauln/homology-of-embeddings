NODE2VEC=~/Downloads/Snap-4.0/examples/node2vec
RIPSER=~/research/libraries/ripser/ripser


FILENAME=sphere
GRAPHFILE=graphs/$FILENAME.edgelist
EMBFILE=embeddings/$FILENAME.emb
TMPBARCODEFILE=barcodes/tmp_$FILENAME.bc
TMPEMBFILE=embeddings/tmp_$FILENAME.emb
BARCODEFILE=barcodes/$FILENAME.json

echo ""
echo "Generate graphs"
python generate_graphs.py

echo ""
echo "Run node2vec on graph"
$NODE2VEC/node2vec -i:$GRAPHFILE -o:$EMBFILE  -l:20 -d:5 -p:1 -dr

python parse_ripser.py trim $EMBFILE $TMPEMBFILE

echo ""
echo "Compute persistent homology on embedding file"
$RIPSER --format point-cloud --dim 1 $TMPEMBFILE > $TMPBARCODEFILE

python parse_ripser.py parse $TMPBARCODEFILE $BARCODEFILE

python visualize.py $BARCODEFILE
