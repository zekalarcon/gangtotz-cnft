<template>

    <div class="modal-overlay" @click="refreshData('modal')">

        <div class="modal" @click.stop>

            <img class="check" src="" alt="" />
            <h6 v-show="selectTittle">SELECT YOUR WALLET</h6>
 
            <div id="wallets">
                <div v-show="walletButtons" v-for="item in list" :class="{ current : item === value }" @click="selectWallet(item)">
                    <label>
                        <div>
                            <button id="item-radio" href="">{{ item }}</button>
                        </div>
                    </label>
                </div>       
            </div>

            <div v-show="loading">
                <svg version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
                    viewBox="0 0 200 300" style="enable-background:new 0 0 200 300;" xml:space="preserve">

                    <rect x="0" class="bg" width="202" height="300" />

                    <defs>
                        <linearGradient id="white-fill" x1="0.5" y1="1" x2="0.5" y2="0">
                            <stop offset="100%" stop-color="#FFF">
                                <animate dur="4s" attributeName="offset" fill="freeze" values="0;1" repeatCount="indefinite" />
                            </stop>
                            <stop offset="100%" stop-color="#000">
                                <animate dur="4s" attributeName="offset" fill="freeze" from="0" to="1" repeatCount="indefinite" />
                            </stop>
                        </linearGradient>
                    </defs>

                    <path class="path" fill="url(#white-fill)" d="M175.38,151.37c-0.12-0.71-0.21-1.39-0.18-2.12c0.07-2.13-0.65-3.78-2.75-4.74c-1.6-0.73-3.31-1.26-4.75-2.36
                        c-1.91-1.46-3.83-2.9-5.62-4.51c-3.27-2.95-6.94-5.42-10.22-8.35c-0.97-0.87-2.03-1.68-2.74-2.79c-1.85-2.9-4.17-5.39-6.99-7.34
                        c-2.4-1.66-5.04-2.73-7.78-3.54c-0.21-1.16-0.8-1.93-1.94-2.22c-0.73-0.19-1.48-0.29-2.22-0.38c-0.01-0.01-0.02-0.01-0.02-0.02
                        c-0.05,0-0.1,0-0.15,0c-1.17-0.13-2.34-0.23-3.5-0.49c-0.37-0.08-2.32,0.16-2.54,0.23c-0.36,0.12-0.87,0.64-0.93,1.03
                        c-0.57-0.03-1.14-0.07-1.71-0.13c4.15-2.67,9.91-6,13.17-9.81c0.26-0.31,0.4-0.7,0.37-1.1c-0.12-1.75-0.59-5.84-0.71-7.19
                        c-0.01-0.06-0.01-0.13-0.01-0.19c1.91-0.67,3.4-1.86,4.67-3.3c-0.15,0.38-0.11,0.4,0.04,0.7c1.34,2.74,3.11,6.24,3.82,9.23
                        c0.08,0.34,0.19,0.72,0.63,0.69c0.44-0.03,0.59-0.39,0.65-0.79c0.34-2.31,0.16-4.59-0.31-6.87c-0.35-1.73-1.21-3.21-2.24-4.71
                        c1.78,0.04,2.91,0.98,3.8,2.23c0.99,1.4,1.89,2.86,2.83,4.29c0.23,0.35,0.37,0.9,0.93,0.71c0.54-0.18,0.42-0.72,0.39-1.13
                        c-0.24-3.16-1.22-6.02-3.54-8.29c-0.5-0.49-1.05-0.94-1.53-1.37c2.42-2.69,4.32-5.7,5.41-9.09c1.35-4.21,0.66-8.39-0.81-12.51
                        c-1.48-4.15-3.59-7.99-6.12-11.55c-0.54-0.75-0.79-1.22-0.79-1.22c1.31-1.1,1.32-3,1.29-3.59c-0.02-0.56-0.12-1.34-0.27-1.85
                        c0,0,0.29-0.15,1.1-0.54c5.63-2.74,8.25-8.73,6.17-14.46c-2.84-7.83-10.67-12.44-19.34-10.15c-6.43,1.7-9.22,6.13-8.16,12.65
                        c0.07,0.45-0.11,0.49-0.45,0.58c-1.22,0.31-2.31,0.91-2.89,2.03c-0.35,0.69-0.75,0.71-1.38,0.66c-3.45-0.26-6.92-0.33-10.36,0.07
                        c-3.89,0.46-7.7,1.35-11.53,2.19c-7.8,1.73-14.23,5.59-19.21,11.86c-1.48,1.86-2.73,3.74-3.32,6.15c-0.73,3-0.45,5.78,0.62,8.49
                        c-0.12,0.45-0.2,0.88-0.22,1.26c-0.32,6.69,0.5,12.75,0.65,13.95c0.3,2.34,1.18,16.58,1.55,21.33c0.14,1.83,0.63,3.53,1.63,5.08
                        c1.51,2.33,3.45,4.26,5.48,6.12c1.75,1.6,3.63,3.04,5.5,4.49c0.67,0.52,1.36,0.89,2.13,1.05c-0.01,0.03-0.03,0.06-0.04,0.08
                        c-0.02,0.09-0.06,0.16-0.08,0.25c-2.03,0.83-4.06,1.68-6.08,2.55c-5.59,2.41-10.98,8.37-10.43,15.72c0.07,0.88-0.31,1.62-0.5,2.43
                        c-1.16,4.83-3.74,9.19-4.72,14.12c-1.22-0.79-2.57-1.17-3.93-1.52c-1.87-0.48-3.71-1.04-5.38-2.07c-0.36-0.22-0.53-0.42-0.47-0.88
                        c0.12-0.89,0.18-1.8,0.21-2.7c0.09-3.06-0.76-5.96-1.42-8.91c-0.23-1.05-0.69-1.85-1.5-2.48c-0.76-0.59-1.52-1.2-2.32-1.74
                        c-0.9-0.61-1.9-0.88-3-0.82c-0.8,0.04-1.58,0.9-2.23,0.5c-0.62-0.38-0.86-1.33-1.33-1.99c-1.27-1.77-2.11-2.05-4.16-1.31
                        c-2.62,0.95-5.32,1.29-8.08,1.23c-0.93-0.02-1.59,0.31-2.21,0.98c-1.16,1.26-1.72,2.84-2.17,4.41c-0.37,1.28-1.04,2.1-2.13,2.74
                        c-0.98,0.58-1.46,1.51-1.26,2.62c0.3,1.67-0.02,3.1-1.06,4.46c-0.75,0.99-1.18,2.21-0.78,3.44c0.43,1.33,0.27,2.56-0.21,3.79
                        c-0.65,1.67-0.1,3.04,0.99,4.3c0.71,0.83,1.45,1.64,2.17,2.46c3.13,3.56,6.91,6,11.68,6.63c1.52,0.2,2.77,0.72,3.74,1.96
                        c0.5,0.65,1.23,1.13,2.11,1.03c1.41-0.16,2.48,0.52,3.47,1.33c1.92,1.59,3.81,3.23,5.7,4.86c2.46,2.12,4.93,4.26,7.83,5.73
                        c2.62,1.33,5.46,2.23,8.04,3.68c1.1,0.62,2.24,0.32,3.3-0.27c1.21-0.68,2.35-1.44,3.39-2.32c-0.26,1.63-0.56,3.26-1.03,4.87
                        c-0.36,1.25-0.91,1.94-2.06,2.44c-1.74,0.76-2.17,1.62-1.94,3.46c0.15,1.15,0.49,2.25,0.94,3.32c0.24,0.58,0.67,0.99,1.27,1.17
                        c0.43,0.13,0.54,0.31,0.52,0.79c-0.06,1.2-0.11,2.39-0.15,3.59c-0.16,0.35-0.17,0.72-0.03,1.1c-0.04,1.15-0.07,2.31-0.08,3.46
                        c0,0.82-0.25,1.32-0.91,1.76c-0.93,0.62-1.82,1.32-2.71,2c-0.31,0.23-0.58,0.52-0.46,0.95c0.14,0.46,0.53,0.61,0.96,0.6
                        c0.4-0.01,0.82-0.04,1.2-0.15c0.55-0.15,1.12-0.12,1.67-0.19c0.41-0.05,0.55,0.09,0.57,0.49c0.04,0.62,0.11,1.25,0.24,1.85
                        c0.24,1.1,0.99,1.35,1.79,0.63c-0.08,1.18-0.28,2.33-0.48,3.49c-0.33,1.91-0.81,3.87-0.39,5.75c0.29,1.29,0.47,2.59,0.6,3.9
                        c-0.97,0.43-1.97,0.8-3.01,1.13c-0.94,0.3-1.48,0.71-1.82,1.62c-0.52,1.38-2.09,4.04-1.77,4.8s0.99,0.65,2.87-0.85
                        c0.41,2.14,0.81,4.25,1.22,6.34c0.17,0.86,0.33,1.72,0.58,2.55c0.26,0.86,0.11,1.59-0.46,2.27c-0.32,0.38-0.6,0.8-0.91,1.19
                        c-0.37,0.46-0.59,0.93-0.67,1.41c-0.31,0.54-0.56,1.1-0.7,1.7c-0.19,0.75-0.5,1.16-1.26,1.38c-0.88,0.26-1.5,0.87-1.53,1.89
                        c-0.05,1.48-0.06,1.48-1.52,1.84c-1.23,0.3-1.68,0.74-1.71,2.03c-0.02,0.87-0.44,1.05-1.14,1.01c-0.24-0.01-0.48-0.15-0.72-0.19
                        c-1.5-0.25-1.74-0.13-2.49,1.4c-0.24,0.49-0.58,0.68-1.03,0.38c-1.62-1.08-3.36-0.67-5.08-0.49c-3.56,0.36-6.26,2.2-8.45,4.9
                        c-0.25,0.3-0.33,0.66-0.35,1.04c-0.12,1.56-0.28,3.11-0.4,4.66c-0.13,1.66,0.65,2.5,1.95,3.25c3.56,2.03,7.43,2.86,11.45,3.11
                        c4.61,0.28,9.23,0.34,13.86,0.07c2.74-0.16,5.51,0.03,8.23-0.22c3.18-0.29,6.33-0.65,9.5-0.13c1.3,0.21,2.61,0.28,4.13,0.25
                        c1.7,0.24,3.51-0.21,5.3-0.79c2.86-0.93,3.53-2.05,3.05-5.02c-0.2-1.25-0.44-2.48-0.37-3.75c0.09-0.37,0.14-0.74,0.15-1.11
                        c0.03-0.15,0.06-0.31,0.11-0.46c0.5-1.72-0.04-3.48-1.43-4.8c-0.73-0.7-1.03-1.52-1.01-2.51c0.02-0.53,0-1.05-0.01-1.58
                        c0.03-0.18,0.05-0.36,0.06-0.54c0.2-0.56,0.34-1.13,0.18-1.76c0.05-0.18,0.11-0.36,0.18-0.53c0.41-1.02-0.04-1.95-0.85-2.41
                        c0.08-0.37,0.23-0.75,0.43-1.14c1.03-2.03,1.97-4.1,2.96-6.15c0.39-0.81,0.54-1.69,0.49-2.55c-0.12-2.22,0.37-4.34,0.93-6.46
                        c0.42-1.62,0.34-3.2-0.32-4.76c-0.34-0.8-0.54-1.66-0.82-2.48c-0.09-0.27-0.04-0.48,0.08-0.71c0.19-0.36,0.32-0.75,0.55-1.08
                        c1.66-2.37,2.07-4.96,1.48-7.75c-0.13-0.61-0.09-1.23-0.16-1.89c0.06-0.24,0.12-0.48,0.18-0.72c0.84,0.28,1.57,0.52,2.3,0.75
                        c0.39,0.12,0.48,0.46,0.58,0.79c0.88,3.05,1.78,6.1,2.6,9.18c0.73,2.71,1.57,5.39,1.74,8.22c0.08,1.38,0.92,2.43,1.69,3.49
                        c0.22,0.3,0.45,0.61,0.67,0.91c0.32,0.59,0.68,1.17,1.11,1.74c0.91,1.19,1.8,2.39,2.69,3.6c0.02,0.04,0.04,0.09,0.07,0.13
                        c0.08,0.18,0.16,0.37,0.25,0.54c0.23,0.59,0.38,1.21,0.39,1.9c0.01,0.63,0.26,1.27,0.7,1.7c0.45,0.43,0.72,0.9,0.86,1.38
                        c-0.03,0.89-0.12,1.77-0.26,2.64c-0.11,0.33-0.21,0.66-0.27,0.98c-0.66-0.76-1.66-0.78-2.37-0.02c-0.45,0.48-0.59,1.1-0.58,1.73
                        c0.02,0.82,0.2,1.61,0.51,2.37c0.96,2.37,1.94,4.73,3.33,6.9c0.45,0.7,0.86,1.4,0.46,2.27c-1.02,2.23-0.85,4.44-0.37,6.72
                        c0,0.78,0.21,1.47,0.61,2.04c0.63,1.29,1.73,1.9,3.2,2.14c1.35,0.21,2.72,0.35,4.1,0.36c2.18,0.02,4.37,0.15,6.55,0.24
                        c6.75,0.28,13.48,0.02,20.18-0.89c1.11-0.15,1.66-0.74,1.94-1.72c0.43-1.52,0.46-3.09,0.34-4.65c-0.07-0.82-0.42-1.52-1.14-2.05
                        c-2.61-1.93-5.12-4.01-8.2-5.19c-0.33-0.48-0.64-0.98-0.94-1.48c0-0.02,0-0.04-0.01-0.05c0.05-0.19,0.07-0.4,0.02-0.64
                        c-0.12-0.6-0.21-1.21-0.32-1.81c-0.08-0.41-0.11-0.82-0.13-1.24c0.01-0.02,0-0.04,0.01-0.05c0.27-0.86,0.11-1.86,0.1-2.8
                        c0-1.2-0.2-2.37-0.65-3.48c-0.3-0.72-0.74-1.11-1.24-1.17c-0.19-0.59-0.38-1.26-0.51-1.95c-0.02-1.01-0.03-2.02-0.01-3.04
                        c0.06-2.84-0.05-5.68-0.35-8.51c-0.26-2.49-0.35-4.96-0.2-7.46c0.15-2.52,0.34-5.09-0.18-7.57c-1.26-6.01-1.85-12.11-2.79-18.16
                        c-0.03-0.18-0.13-0.4,0.2-0.57c0.26-0.13,0.28-0.06,0.51,0.12c0.66,0.51,1.42,0.59,2.22,0.36c0.95-0.28,1.74-0.83,2.4-1.56
                        c0.77-0.86,1.54-1.72,2.33-2.56c1.34-1.42,2.47-2.96,2.49-5.07c0.03-2.84,0.4-5.66,0.42-8.51c0.01-1.25,0.22-2.48,1.54-3.17
                        c0.55-0.29,0.91-0.87,1-1.52c0.22-1.57,1.1-2.77,2.23-3.78c1.75-1.56,3.52-3.09,5.31-4.6c4.03-3.42,7.3-7.4,9.27-12.37
                        C175.38,158.73,175.99,155.12,175.38,151.37z M141.79,162.63c-0.2-2.88-0.41-5.75-0.18-8.63c0.01,0.01,0.02,0.02,0.03,0.04
                        c1.59,1.64,3.23,3.2,5.47,3.94c0.21,0.07,0.4,0.17,0.27,0.47c-1.78,4.28-2.94,8.8-5.02,12.96c0.01-0.12,0.01-0.24,0.02-0.39
                        C142.55,168.19,141.99,165.42,141.79,162.63z M73.73,256.2 M72.32,255.61 M140.05,90.48c0.02,0.02,0.04,0.04,0.06,0.06
                        c-0.26,0.79-0.49,1.18-0.79,1.59c-0.1-0.1-0.2-0.21-0.31-0.31C139.37,91.4,139.72,90.95,140.05,90.48z M63.54,260.83
                        c0.03-0.06,0.07-0.09,0.1-0.13c-0.01,0.03-0.03,0.05-0.04,0.08c-0.1,0.24-0.11,0.45-0.07,0.64
                        C63.45,261.24,63.44,261.04,63.54,260.83z" />

                </svg>
            </div>

            <div v-show="minted" id="minted-text">
                GangTot minted! Check your wallet. <br>
                Might take a few minutes. <br>
                Thanks for being part of the GangTotz community!
            </div>
            
            <div id="purchase-button" v-show="purchaseButton">
                <a class="cta" @click="buildTx()">BUY</a>
            </div>       

        </div>
        
        <div class="close" @click="refreshData('modal')">
            <img class="close-img" src="" alt="" />
        </div>

    </div>
</template>


<script>

import {
    Address,
    TransactionUnspentOutput,
    TransactionUnspentOutputs,
    TransactionOutput,
    Value,
    TransactionBuilder,
    TransactionBuilderConfigBuilder,
    LinearFee,
    BigNum,
    TransactionWitnessSet,
    Transaction
} from "@emurgo/cardano-serialization-lib-asmjs"

let Buffer = require('buffer/').Buffer;

import axios from 'axios'

export default {
    name: 'WalletModal',
    data() {
        return {
            value: '',
			list: [],
            nfts: [],
            loading: false,
            walletButtons: true,
            purchaseButton: false,
            minted: false,
            selectTittle: true,
            constructor: {
                whichWalletSelected: undefined,
                walletIsEnabled: false,
                walletName: undefined,
                Utxos: undefined,
                CollatUtxos: undefined,
                changeAddress: undefined,
                usedAddress: undefined,
                submittedTxHash: "",
                addressBech32SendADA: "addr1q8lyeuw6lac994uqdrgrzjr330a88nnd0hgzrquqsqdaw6z3h7uvtztmhjn2gdc9dsp8qsyuksn053w7ysq2xkxem95qlatym9",
                lovelaceToSend: 6000000,
                nftId: undefined
            },
            protocolParams: {
                linearFee: {
                    minFeeA: "44",
                    minFeeB: "155381",
                },
                minUtxo: "34482",
                poolDeposit: "500000000",
                keyDeposit: "2000000",
                maxValSize: 5000,
                maxTxSize: 16384,
                priceMem: 0.0577,
                priceStep: 0.0000721,
                coinsPerUtxoWord: "34482",
            },
            api: undefined,
            isLoading: false
        }
    },
    components: { 
    },
    mounted() {
        this.getwallets() 
    },
    methods: {       
        getwallets(count=0) {
            const wallets = [];
            for(const key in window.cardano) {
                if (window.cardano[key].enable && wallets.indexOf(key) === -1) {
                    if (key != 'ccvault'){
                        wallets.push(key);
                    }else{
                        
                    }
                }    
            }
            if (wallets.length === 0 && count < 3) {
                setTimeout(() => {
                    count + 1;
                }, 1000);
                return;
            }
            this.list = wallets
            //console.log('Wallets: ', wallets)
        },
        selectWallet(option) {
            this.refreshData('select wallet');
            this.walletButtons = false;
            this.value = option;
            this.constructor.whichWalletSelected = option;
            this.selectTittle = false;
            this.enableWallet();
        },
        /**
         * Checks if a connection has been established with
         * the wallet
         * @returns {Promise<boolean>}
        */
        async checkIfWalletEnabled() {
            let walletIsEnabled = false;

            try {
                const walletName = this.constructor.whichWalletSelected;
                walletIsEnabled = await window.cardano[walletName].isEnabled();
            } catch (err) {
                //console.log(err)
                console.log('wallet not enable')
            }
            this.constructor.walletIsEnabled = walletIsEnabled;

            return walletIsEnabled;
        },
        /**
         * Enables the wallet that was chosen by the user
         * When this executes the user should get a window pop-up
         * from the wallet asking to approve the connection
         * of this app to the wallet
         * @returns {Promise<boolean>}
        */
        async enableWallet() {
            const walletKey = this.constructor.whichWalletSelected;
            try {
                this.loading = true;
                this.api = await window.cardano[walletKey].enable();
                await this.getUtxos();
                await this.getChangeAddress();
                await this.getUsedAddresses();
                this.loading = false;
                this.purchaseButton = true;
            } catch(err) {
                this.refreshData();
                console.log(err);
            }
            return this.checkIfWalletEnabled();
        },
        /**
         * Gets the UTXOs from the user's wallet and then
         * stores in an object in the state
         * @returns {Promise<void>}
        */
        async getUtxos() {
            let Utxos = [];
            try {
                const rawUtxos = await this.api.getUtxos();
                for (const rawUtxo of rawUtxos) {
                    const utxo = TransactionUnspentOutput.from_bytes(Buffer.from(rawUtxo, "hex"));
                    const input = utxo.input();
                    const txid = Buffer.from(input.transaction_id().to_bytes(), "utf8").toString("hex");
                    const txindx = input.index();
                    const output = utxo.output();
                    const amount = output.amount().coin().to_str(); // ADA amount in lovelace
                    const multiasset = output.amount().multiasset();
                    let multiAssetStr = "";
                    if (multiasset) {
                        const keys = multiasset.keys() // policy Ids of thee multiasset
                        const N = keys.len();
                        //console.log(`${N} Multiassets in the UTXO`)
                        for (let i = 0; i < N; i++){
                            const policyId = keys.get(i);
                            const policyIdHex = Buffer.from(policyId.to_bytes(), "utf8").toString("hex");
                            // console.log(`policyId: ${policyIdHex}`)
                            const assets = multiasset.get(policyId)
                            const assetNames = assets.keys();
                            const K = assetNames.len()
                            // console.log(`${K} Assets in the Multiasset`)
                            for (let j = 0; j < K; j++) {
                                const assetName = assetNames.get(j);
                                const assetNameString = Buffer.from(assetName.name(),"utf8").toString();
                                const assetNameHex = Buffer.from(assetName.name(),"utf8").toString("hex")
                                const multiassetAmt = multiasset.get_asset(policyId, assetName)
                                multiAssetStr += `+ ${multiassetAmt.to_str()} + ${policyIdHex}.${assetNameHex} (${assetNameString})`
                                // console.log(assetNameString)
                                // console.log(`Asset Name: ${assetNameHex}`)
                            }
                        }
                    }
                    const obj = {
                        txid: txid,
                        txindx: txindx,
                        amount: amount,
                        str: `${txid} #${txindx} = ${amount}`,
                        multiAssetStr: multiAssetStr,
                        TransactionUnspentOutput: utxo
                    }
                    Utxos.push(obj);
                    //console.log('utxo:',obj )
                }
                this.constructor.Utxos = Utxos;
                console.log('getUtxos ok')
                //this.getCollateral();
            } catch (err) {
                console.log(err)
            }
            
        },
        async getCollateral() {
            let CollatUtxos = [];
            try {
                let collateral = [];
                const wallet = this.constructor.whichWalletSelected;
                if (wallet === "Flint") {
                    collateral = await this.api.experimental.getCollateral();
                } else {
                    collateral = await this.api.getCollateral();
                }
                for (const x of collateral) {
                    const utxo = TransactionUnspentOutput.from_bytes(Buffer.from(x, "hex"));
                    CollatUtxos.push(utxo)
                    // console.log(utxo)
                }
                this.constructor.CollatUtxos = CollatUtxos
                console.log('Collateral: ', this.constructor.CollatUtxos);
            } catch (err) {
                console.log(err)
            }
            
        },
        /**
         * Gets previsouly used addresses
         * @returns {Promise<void>}
        */
        async getUsedAddresses() {

            try {
                const raw = await this.api.getUsedAddresses();
                const rawFirst = raw[0];
                const usedAddress = Address.from_bytes(Buffer.from(rawFirst, "hex")).to_bech32()
                this.constructor.usedAddress = usedAddress

            } catch (err) {
                console.log(err)
            }
        },
        /**
         * Get the address from the wallet into which any spare UTXO should be sent
         * as change when building transactions.
         * @returns {Promise<void>}
        */
        async getChangeAddress() {
            try {
                const raw = await this.api.getChangeAddress();
                const changeAddress = Address.from_bytes(Buffer.from(raw, "hex")).to_bech32()
                this.constructor.changeAddress = changeAddress
                //console.log('change addr ok')
            } catch (err) {
                console.log(err)
            }
        },
        /**
         * Every transaction starts with initializing the
         * TransactionBuilder and setting the protocol parameters
         * This is boilerplate
         * @returns {Promise<TransactionBuilder>}
        */
        async initTransactionBuilder() {

            const txBuilder = TransactionBuilder.new(
                TransactionBuilderConfigBuilder.new()
                    .fee_algo(LinearFee.new(BigNum.from_str(this.protocolParams.linearFee.minFeeA), BigNum.from_str(this.protocolParams.linearFee.minFeeB)))
                    .pool_deposit(BigNum.from_str(this.protocolParams.poolDeposit))
                    .key_deposit(BigNum.from_str(this.protocolParams.keyDeposit))
                    .coins_per_utxo_word(BigNum.from_str(this.protocolParams.coinsPerUtxoWord))
                    .max_value_size(this.protocolParams.maxValSize)
                    .max_tx_size(this.protocolParams.maxTxSize)
                    .prefer_pure_change(true)
                    .build()
            );

            return txBuilder
        },

        /**
         * Builds an object with all the UTXOs from the user's wallet
         * @returns {Promise<TransactionUnspentOutputs>}
        */
        async getTxUnspentOutputs() {
            let txOutputs = TransactionUnspentOutputs.new()
            for (const utxo of this.constructor.Utxos) {
                txOutputs.add(utxo.TransactionUnspentOutput)
            }
            return txOutputs
        },

        /**
         * The transaction is build in 3 stages:
         * 1 - initialize the Transaction Builder
         * 2 - Add inputs and outputs
         * 3 - Calculate the fee and how much change needs to be given
         * 4 - Build the transaction body
         * 5 - Sign it (at this point the user will be prompted for
         * a password in his wallet)
         * 6 - Send the transaction
         * @returns {Promise<void>}
         */
        async buildSendADATransaction() {
            try{
                const txBuilder = await this.initTransactionBuilder();
                const shelleyOutputAddress = Address.from_bech32(this.constructor.addressBech32SendADA);
                const shelleyChangeAddress = Address.from_bech32(this.constructor.changeAddress);

                txBuilder.add_output(
                    TransactionOutput.new(
                        shelleyOutputAddress,
                        Value.new(BigNum.from_str(this.constructor.lovelaceToSend.toString()))
                    ),
                );

                // Find the available UTXOs in the wallet and
                // us them as Inputs
                const txUnspentOutputs = await this.getTxUnspentOutputs();
                txBuilder.add_inputs_from(txUnspentOutputs, 0)

                // calculate the min fee required and send any change to an address
                txBuilder.add_change_if_needed(shelleyChangeAddress)

                // once the transaction is ready, we build it to get the tx body without witnesses
                const txBody = txBuilder.build();


                // Tx witness
                const transactionWitnessSet = TransactionWitnessSet.new();

                const tx = Transaction.new(
                    txBody,
                    TransactionWitnessSet.from_bytes(transactionWitnessSet.to_bytes())
                )

                let txVkeyWitnesses = await this.api.signTx(Buffer.from(tx.to_bytes(), "utf8").toString("hex"), true);

                //console.log(txVkeyWitnesses)

                txVkeyWitnesses = TransactionWitnessSet.from_bytes(Buffer.from(txVkeyWitnesses, "hex"));

                transactionWitnessSet.set_vkeys(txVkeyWitnesses.vkeys());

                const signedTx = Transaction.new(
                    tx.body(),
                    transactionWitnessSet
                );

                const submittedTxHash = await this.api.submitTx(Buffer.from(signedTx.to_bytes(), "utf8").toString("hex"));
                //console.log(submittedTxHash)
                this.constructor.submittedTxHash = submittedTxHash;
                this.mintNft();
            }catch {
                if(this.constructor.nftId != undefined){
                    this.unlockNft();
                }else{

                }
                alert('error');
            }
        },
        async refreshData(data) {
           
            if(data == 'modal'){
                if(this.constructor.nftId != undefined){
                    this.unlockNft();
                    this.$emit('close-modal');
                }else{
                    this.$emit('close-modal');
                }
            }else{

            }

            this.walletButtons = true;
            this.purchaseButton = false;
            this.loading = false;
            this.minted = false;
            this.selectTittle = true;
            
            this.constructor.whichWalletSelected = undefined;
            this.constructor.walletIsEnabled = false;
            this.constructor.walletName = undefined;
            this.constructor.Utxos = undefined;
            this.constructor.CollatUtxos = undefined;
            this.constructor.changeAddress = undefined;
            this.constructor.usedAddress = undefined;
            this.constructor.submittedTxHash = "";
            this.constructor.nftId = undefined;

        },
        async buildTx() {
            
            // Private code        
        },
        async unlockNft() {

            let post={
                id: this.constructor.nftId
            };
           
            axios.post("unlock_nft/", post).then((result) => {
                console.log(result);
            });
            
        },
        async mintNft() {
            // Private code
            
        },
        

        
    }
}
</script>

<style scoped>

@import url('https://fonts.googleapis.com/css2?family=Luckiest+Guy&display=swap');

#minted-text{
    font-family: 'Luckiest Guy';
    font-size: 24px;
    color: rgb(243, 243, 243);
    margin-top: 15px;
}

.minting p {
  position: relative;
  text-transform: uppercase;
  font-size: 2em;
  letter-spacing: 4px;
  overflow: hidden;
  background: linear-gradient(90deg, #000, #fff, #000);
  background-repeat: no-repeat;
  background-size: 80%;
  animation: animate 3s linear infinite;
  -webkit-background-clip: text;
  -webkit-text-fill-color: rgba(255, 255, 255, 0);
}
@keyframes animate {
  0% {
    background-position: -500%;
  }
  100% {
    background-position: 500%;
  }
}

svg{
  width: 100px;
  height: 100px;
  margin: 20px;
  display:inline-block;
}

.bg { fill:none; }
.path { stroke:#FFFFFF; stroke-width:1; stroke-miterlimit: 10; }


/* CTA STYLE */
.cta {
  padding: 18px 23px 18px 23px;
  color: #000000;
  font-size: 15px;
  background-color: #db3636;
  font-weight: 900;
  text-decoration: none;
  clear: both;
  width: 100%;
  text-align: center;
  display: block;
  margin-left: auto;
  margin-right: auto;
  margin-bottom: 20px;
}
.cta:hover { color: #000000; }

#item-radio{
    text-transform: capitalize;
    cursor: pointer;
}

.modal-overlay {
    z-index: 999;
    position: fixed;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    display: flex;
    flex-wrap: wrap;
    align-content: center;
    justify-content: center;
    align-items: flex-end;
    backdrop-filter: hue-rotate(180deg) blur(2px);
    -webkit-backdrop-filter: hue-rotate(180deg) blur(2px);
}

.modal {
    text-align: center;
    background-color: rgba(7, 7, 7, 0.501);
    max-height: 500px;
    width: 356px;
    margin-top: auto;
    margin-bottom: auto;
    border-radius: 20px;
}
.close {
  margin: 10% 0 0 16px;
  cursor: pointer;
}

.close-img {
  width: 25px;
}

.check {
  width: 150px;
}

h6 {
    color: #ffffff;
    font-weight: 900;
    font-size: 20px;
    margin-top: auto;
    margin-bottom: 20px;
}

button {
  background-color: #dfdfdf;
  width: 150px;
  height: 40px;
  color: rgb(0, 0, 0);
  font-size: 14px;
}


</style>
