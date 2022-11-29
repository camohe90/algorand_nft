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

def delete_non_fungible_token():
  # For ease of reference, add account public and private keys to
  # an accounts dict.
    print("--------------------------------------------")
    accounts = {}
    accounts[1] = {}
    accounts[1]['pk'] = MY_ADDRESS
    accounts[1]['sk'] = PRIVATE_KEY

    algod_address = os.environ.get("algod_address")
    algod_token = os.environ.get("algod_token")
    headers = {
    "X-API-Key": algod_token,
    }

    algod_client = algod.AlgodClient(algod_token, algod_address, headers)

    print("--------------------------------------------")
    print("Deleting Asset...")

    # Get network params for transactions before every transaction.
    params = algod_client.suggested_params()
    # comment these two lines if you want to use suggested params
    # params.fee = 1000
    # params.flat_fee = True
    asset_id = int(input("Ingrese el id del asset que desea eliminar: "))


    # Asset destroy transaction
    txn = AssetConfigTxn(
        sender=accounts[1]['pk'],
        sp=params,
        index=asset_id,
        strict_empty_address_check=False
        )

    # Sign with secret key of creator
    stxn = txn.sign(accounts[1]['sk'])
    # Send the transaction to the network and retrieve the txid.
    txid = algod_client.send_transaction(stxn)
    print("Asset Destroy Transaction ID: {}".format(txid))

    # Wait for the transaction to be confirmed
    confirmed_txn = wait_for_confirmation(algod_client, txid, 4)  
    print("TXID: ", txid)
    print("Result confirmed in round: {}".format(confirmed_txn['confirmed-round']))
    # Asset was deleted.
    try:
        print("Asset is deleted.")
    except Exception as e:
        print(e)
    
    print("--------------------------------------------")
    
    #   Utility function used to print created asset for account and assetid

delete_non_fungible_token()