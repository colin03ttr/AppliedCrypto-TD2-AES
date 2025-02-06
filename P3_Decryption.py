import hashlib
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from Crypto.Util.number import long_to_bytes
import time

start_time = time.time()

# ct = AES(k1,AES(k2,pt)) # ECB mode
# it means that myAES_decrypt(k1, ct) = myAES_encrypt(k2, pt)
# table 1: all possible decryption of myAES_encrypt(k1, ct) -> 2^24 possibilities
# table 2: all possible encryption of myAES_decrypt(k2, ct) -> 2^24 possibilities
# 2^24 = 256^3 possibilities for random1 and random2

def myAES_encrypt(key, m):
    if len(m) != 32:
        return b'Invalid block size'
    algorithm = algorithms.AES(key)
    cipher = Cipher(algorithm, mode=modes.ECB(), backend=default_backend())
    encryptor = cipher.encryptor()
    ct = encryptor.update(m) + encryptor.finalize()
    return ct


def myAES_decrypt(key, m):
    if len(m) != 32:
        return b'Invalid block size'
    algorithm = algorithms.AES(key)
    cipher = Cipher(algorithm, mode=modes.ECB(), backend=default_backend())
    decryptor = cipher.decryptor()
    ct = decryptor.update(m) + decryptor.finalize()
    return ct

try_pt = b'This is a non-secret message....'
try_ct = b'7\xcf7\xce\xa6 \xbe\t\xba\x03\xe4\xac\x9e\x86\x85\xf5YZYa_7\xae\xa1\xe6\xc1\xd1\xad\xfb\x9c\x99s'

encs = []
for i in range(256**3):
    k2 = long_to_bytes(i).rjust(3, b'\x00') + b'A'*29
    ct = myAES_encrypt(k2, try_pt)
    encs.append(ct)

for i in range(256**3):
    k1 = long_to_bytes(i).rjust(3, b'\x00') + b'A'*29
    ct = myAES_decrypt(k1, try_ct)
    if ct in encs:
        print(f"Key1: {k1}")
        print(f"Key2: {k2}")
        print(f"Decrypted: {ct}")
        break

sha256 = hashlib.sha256(k1 + k2).hexdigest()
print(f"Flag: {'CTF{'+sha256+'}'}")

end_time = time.time()
print(f"Execution time: {end_time - start_time} seconds")