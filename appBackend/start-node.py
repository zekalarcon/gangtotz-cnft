from cardano_tools import CardanoNode

node = CardanoNode(
    binary= "/home//.local/bin/cardano-node",
    topology= "/home//cardano-src/testnet/testnet-topology.json",
    database_path= "/home//cardano-src/testnet/db",
    socket_path= "/home//cardano-src/testnet/db/node.socket",
    config= "/home//cardano-src/testnet/testnet-config.json",
    show_output=True,  # Optionally print node output to the terminal.
    )
node.start()