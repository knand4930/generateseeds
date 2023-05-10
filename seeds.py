from mnemonic import Mnemonic
import os

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


cred = credentials.Certificate("cryptoseeds-daef1-firebase-adminsdk-pz1q3-980d6ab096.json")
firebase_admin.initialize_app(cred, {'databaseURL':'https://cryptoseeds-daef1-default-rtdb.firebaseio.com/'})
ref = db.reference('py/')


while True:
    random_bytes = os.urandom(16)
    mnemo = Mnemonic("english")
    seed_words = mnemo.to_mnemonic(random_bytes)
    print(seed_words)
   
   # data = ref.get()
    ref.update({'seeds_phrase': seed_words})
    with open('data.txt', 'a') as file:
        file.write('\n' + str(seed_words))
