
export CARDANO_NODE_SOCKET_PATH=~/cardano-src/testnet/db/node.socket

cardano-cli address key-gen \
    --verification-key-file payment.vkey \
    --signing-key-file payment.skey