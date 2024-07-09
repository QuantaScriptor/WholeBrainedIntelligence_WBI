python
from web3 import Web3

# Connect to a blockchain
def connect_to_blockchain():
    web3 = Web3(Web3.HTTPProvider('http://localhost:8545'))
    if web3.isConnected():
        print("Connected to blockchain")
    return web3

# Create a new transaction
def create_transaction(web3, from_address, to_address, value):
    tx = {
        'from': from_address,
        'to': to_address,
        'value': web3.toWei(value, 'ether'),
        'gas': 2000000,
        'gasPrice': web3.toWei('50', 'gwei')
    }
    signed_tx = web3.eth.account.sign_transaction(tx, private_key='YOUR_PRIVATE_KEY')
    tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    return tx_hash

def main():
    web3 = connect_to_blockchain()
    from_address = '0xYourFromAddress'
    to_address = '0xYourToAddress'
    value = 0.1  # in Ether
    tx_hash = create_transaction(web3, from_address, to_address, value)
    print(f"Transaction hash: {tx_hash.hex()}")

if __name__ == "__main__":
    main()
