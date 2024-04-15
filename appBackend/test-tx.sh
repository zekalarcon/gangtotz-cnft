f=$1
oref=$2
name=$3

echo "oref: $oref"

cabal exec token-policy $f $oref 1 $name
