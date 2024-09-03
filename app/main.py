import json
import os
import requests

INFURA_API_KEY = '' or os.environ.get('INFURA_API_KEY')
ETH_MAINNET_URL = f'https://mainnet.infura.io/v3/{INFURA_API_KEY}'

# Default, global headers
headers = {
    'Content-Type': 'application/json',
}

def get_block_number() -> int:
    payload = {
        'jsonrpc': '2.0',
        'method': 'eth_getBlockByNumber',
        'params': ['latest', False],
        'id': 1,
    }

    try:
        response = requests.post(ETH_MAINNET_URL, headers=headers, data=json.dumps(payload))
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error: {err}")

    return int(response.json()['result']['number'], 16)


def get_block_by_number(block_number: int) -> dict:
    payload = {
        'jsonrpc': '2.0',
        'method': 'eth_getBlockByNumber',
        'params': [hex(block_number), True],
        'id': 1,
    }

    try:
        response = requests.post(ETH_MAINNET_URL, headers=headers, data=json.dumps(payload))
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error: {err}")

    return response.json()['result']

# Tests
print(get_block_number())
print(get_block_by_number(get_block_number()))
