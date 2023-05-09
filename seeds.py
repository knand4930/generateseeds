from mnemonic import Mnemonic
import os

while True:
    random_bytes = os.urandom(16)
    mnemo = Mnemonic("english")
    seed_words = mnemo.to_mnemonic(random_bytes)
    print(seed_words)
    with open('data.txt', 'a') as file:
        file.write('\n' + str(seed_words))
