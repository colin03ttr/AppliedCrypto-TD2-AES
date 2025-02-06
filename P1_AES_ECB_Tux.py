from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os



def myAES_encrypt(key, m):
    if len(m) != 16:
        return b'Invalid block size'
    algorithm = algorithms.AES(key)
    cipher = Cipher(algorithm, mode=modes.ECB(), backend=default_backend())
    encryptor = cipher.encryptor()
    ct = encryptor.update(m) + encryptor.finalize()
    return ct


def myAES_decrypt(key, m):
    if len(m) != 16:
        return b'Invalid block size'
    algorithm = algorithms.AES(key)
    cipher = Cipher(algorithm, mode=modes.ECB(), backend=default_backend())
    decryptor = cipher.decryptor()
    ct = decryptor.update(m) + decryptor.finalize()
    return ct

# Generate a random 16-byte AES key
key = os.urandom(16)
print(f"Using AES Key: {key.hex()}")

with open("Tux.body", "rb") as f:
    body_data = f.read()

original_length = len(body_data)
print(f"len of body data: {original_length}")

# Ensure data is a multiple of 16 bytes by padding with null bytes (ECB needs fixed block size)
if len(body_data) % 16 != 0:
    padding_len = 16 - (len(body_data) % 16)
    body_data += b'\x00' * padding_len

# Encrypt in 16-byte blocks
encrypted_data = b''
for i in range(0, len(body_data), 16):
    block = body_data[i:i+16]
    encrypted_data += myAES_encrypt(key, block)

print(f"len of encrypted data: {len(encrypted_data)}")
with open("Tux.body.ecb", "wb") as f:
    f.write(encrypted_data)

print("Encrypted Tux.body to Tux.body.ecb")

# Decrypt in 16-byte blocks
decrypted_data = b''
for i in range(0, len(encrypted_data), 16):
    block = encrypted_data[i:i+16]
    decrypted_data += myAES_decrypt(key, block)

# **Truncate decrypted data back to original length**
decrypted_data = decrypted_data[:original_length]
print(f"len of decrypted data: {len(decrypted_data)}")

with open("Tux.body.dec", "wb") as f:
    f.write(decrypted_data)

print("Decrypted Tux.body.ecb to Tux.body.dec")