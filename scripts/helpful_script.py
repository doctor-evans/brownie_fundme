from brownie import accounts, MockV3Aggregator, config, network
from web3 import Web3

LOCAL_BLOCKCHAIN_ENVIRONMENT = ["development", "ganache-local"]

DECIMAL = 8
STARTING_PRICE = 200000000000


def get_account():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENT:
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_mocks():
    print(f"The active network is {network.show_active()}")
    print("Deploying mocks...")
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(
            DECIMAL, Web3.toWei(STARTING_PRICE, "ether"), {"from": get_account()}
        )
    print("Mocks deployed")
