import requests
import datetime


def unix_time():
    current_time = datetime.datetime.now()
    timestamp = datetime.datetime.timestamp(current_time)
    return timestamp


def get_balance(address, api_key):
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
    return response


def get_total_gas_used():
    pass


address = input('Ethereum Address: ')
etherscan_api_key = '3SVXH4QK42N8XZN5BY6BDM9687TN1GMA9K'
print(f'Balance: {get_balance(metamask_address, etherscan_api_key)} eth')
print(get_current_block(etherscan_api_key))


#TODO: fix unix_time calculation