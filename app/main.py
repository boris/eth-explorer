import os
from web3 import Web3
from flask import Blueprint, redirect, url_for, render_template

INFURA_API_KEY = '' or os.environ.get('INFURA_API_KEY')
ETH_MAINNET_URL = f'https://mainnet.infura.io/v3/{INFURA_API_KEY}'
web3 = Web3(Web3.HTTPProvider(ETH_MAINNET_URL))

main = Blueprint('main', __name__)

def web3_latest_block():
    latest_block = web3.eth.block_number
    print(f"Latest block: {latest_block}")

    latest_10_blocks = []

    for i in range(latest_block, latest_block - 10, -1):
        block = web3.eth.get_block(i)
        latest_10_blocks.append(block)

    return latest_block, latest_10_blocks

@main.route('/')
def hello_world():
    latest_block = web3_latest_block()
    return render_template('index.html', 
                           latest_block=latest_block[0],
                           latest_10_blocks=latest_block[1],
                           )

@main.route('/block/<int:block_number>')
def block(block_number):
    block = web3.eth.get_block(block_number)
    return render_template('block.html', block=block)

@main.route('/health')
def health():
    if web3 is not None:
        return 'Healthy', 200
    else:
        return 'Unhealthy', 500
