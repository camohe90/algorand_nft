import json
import hashlib
import os
from algosdk import mnemonic
from algosdk.v2client import algod
from algosdk.future.transaction import AssetConfigTxn, wait_for_confirmation
from dotenv import load_dotenv


def create_hash():
  
    dir_path = os.path.dirname(os.path.realpath(__file__))
    f = open (dir_path + '/data.json', "r")
    
  # Reading from file
    metadataJSON = json.loads(f.read())

    metadataStr = json.dumps(metadataJSON)


    hash = hashlib.new("sha512_256")

    hash.update(b"arc0003/amj")

    hash.update(metadataStr.encode("utf-8"))
    json_metadata_hash = hash.digest()
    print(json_metadata_hash)
   


create_hash()