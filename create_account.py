
from algosdk import account, mnemonic

def generate_algorand_keypair():
    private_key, address = account.generate_account()
    print(f"My address: {address}")
    print(f"My private key: {private_key}")
    print(F"My passphrase: {mnemonic.from_private_key(private_key)}")


generate_algorand_keypair()