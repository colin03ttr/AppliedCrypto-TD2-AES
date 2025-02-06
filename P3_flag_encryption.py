import os
from Crypto.Cipher import AES

random1 = os.urandom(3)
random2 = os.urandom(3)

k1 = random1 + b"A"*29
k2 = random2 + b"A"*29
plain = b'This is a non-secret message....'

cipher = AES(k1,AES(k2,plain)) # ECB mode

print(cipher)