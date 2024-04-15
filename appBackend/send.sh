
export CARDANO_NODE_SOCKET_PATH=~/cardano-src/testnet/db/node.socket

cardano-cli transaction build \
    --babbage-era \
    --testnet-magic 1097911063 \
    --change-address  \
    --tx-in f#0 \
    --tx-out " + 100000000 lovelace" \
    --out-file tx.body

cardano-cli transaction sign \
    --tx-body-file tx.body \
    --signing-key-file testnet/01.skey \
    --testnet-magic 1097911063 \
    --out-file tx.signed

cardano-cli transaction submit \
    --testnet-magic 1097911063 \
    --tx-file tx.signed
