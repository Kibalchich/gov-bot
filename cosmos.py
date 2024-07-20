import requests
from cosmospy import generate_wallet, seed_to_privkey, privkey_to_address
import base64
import json

BOT_WALLET_MNEMONIC = "claw 