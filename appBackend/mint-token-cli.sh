#!/bin/bash

oref=$1
tn=$2
addrFile=$3
skeyFile=$4
amt=1

echo "oref: $oref"
echo "amt: $amt"
echo "tn: $tn"
echo "address file: $addrFile"
echo "signing key file: $skeyFile"

ppFile=testnet/protocol-parameters.json
#cardano-cli query protocol-parameters --testnet-magic 1097911063 --out-file $ppFile

policyFile=testnet/policy.plutus
#cabal exec token-policy $policyFile $oref $amt $tn

unsignedFile=testnet/tx.unsigned
signedFile=testnet/tx.signed
pid=$(cardano-cli transaction policyid --script-file $policyFile)
tnHex=$(cabal exec token-name -- $tn)
addr=$(cat $addrFile)
v="$amt $pid.$tnHex"

echo "currency symbol: $pid"
echo "token name (hex): $tnHex"
echo "minted value: $v"
echo "address: $addr"

cardano-cli transaction build \
    --testnet-magic 1097911063 \
    --tx-in $oref \
    --tx-in-collateral $oref \
    --tx-out "addr_test1qq6eawpguk2mkusk2s8lstjtjsahl2xtvz78cqxn2tj4sj8ap6jnmvursz4kywzs79d5aeqja8xwgqad20jcgy4wk95qvkjr3a + 2000000 lovelace + $v" \
    --mint "$v" \
    --mint-script-file $policyFile \
    --metadata-json-file metadata.json \
    --mint-redeemer-file testnet/unit.json \
    --change-address $addr \
    --protocol-params-file $ppFile \
    --out-file $unsignedFile \

cardano-cli transaction sign \
    --tx-body-file $unsignedFile \
    --signing-key-file $skeyFile \
    --testnet-magic 1097911063 \
    --out-file $signedFile

cardano-cli transaction submit \
    --testnet-magic 1097911063 \
    --tx-file $signedFile
