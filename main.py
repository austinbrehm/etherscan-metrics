import requests
from datetime import datetime


def unix_time():
    current_time = datetime.now()
    timestamp = int(current_time.timestamp())
    return timestamp


def get_balance(api_key, address):
    api_url = 'https://api.etherscan.io/api' \
              '?module=account' \
              '&action=balance' \
              f'&address={address}' \
              '&tag=latest' \
              f'&apikey={api_key}'
    response = requests.get(api_url).json()
    balance_eth = round(float(response['result']) * 10**-18, 10)
    return balance_eth


def get_current_block(api_key):
    timestamp = str(unix_time())
    api_url = 'https://api.etherscan.io/api' \
              '?module=block' \
              '&action=getblocknobytime' \
              f'&timestamp={timestamp}' \
              '&closest=before' \
              f'&apikey={api_key}'
    response = requests.get(api_url).json()
    current_block = response['result']
    return current_block


def get_total_gas_used(api_key, address, number_of_transactions):
    api_url = 'https://api.etherscan.io/api' \
              '?module=account' \
              '&action=txlist' \
              f'&address={address}' \
              '&startblock=0' \
              f'&endblock={get_current_block(api_key)}' \
              '&page=1' \
              f'&offset={number_of_transactions}' \
              '&sort=asc' \
              f'&apikey={api_key}'
    response = requests.get(api_url).json()
    result = response['result']
    total_gas = 0
    for transaction in result:
        gas = int(transaction['gasPrice']) * int(transaction['gasUsed'])
        total_gas += gas
    total_gas_eth = total_gas * 10**-18
    return total_gas_eth


eth_address = input('Ethereum Address: ')
etherscan_api_key = '3SVXH4QK42N8XZN5BY6BDM9687TN1GMA9K'

print(f'Balance: {get_balance(etherscan_api_key, eth_address)} eth')
print(f'Block: {get_current_block(etherscan_api_key)}')
print(f'Total gas used: {round(get_total_gas_used(etherscan_api_key, eth_address, 100), 10)} eth')


#TODO: fix unix_time calculation