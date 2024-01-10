import json
import hashlib
import os
from algosdk import mnemonic
from algosdk.v2client import algod
from algosdk.future.transaction import AssetConfigTxn, wait_for_confirmation
from dotenv import load_dotenv

load_dotenv()

MY_ADDRESS = os.environ.get("MY_ADDRESS")
PRIVATE_KEY = os.environ.get("PRIVATE_KEY")
PASSPHRASE = os.environ.get("PASSPHRASE")

def account_info():
  # For ease of reference, add account public and private keys to
  # an accounts dict.
    print("--------------------------------------------")
    accounts = {}
    accounts[1] = {}
    accounts[1]['pk'] = MY_ADDRESS
    accounts[1]['sk'] = PRIVATE_KEY

    algod_address = os.environ.get("TESTNET_URL")
    algod_token = os.environ.get("API_TOKEN")
    headers = {
    "X-API-Key": algod_token,
    }

    algod_client = algod.AlgodClient(algod_token, algod_address, headers)

    account_information = algod_client.account_info(accounts[1]['pk'])
    print(account_information)
    print(account_information['assets'])

    

account_info()