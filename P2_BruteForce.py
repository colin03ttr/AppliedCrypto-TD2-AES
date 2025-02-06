import random

ciphertext_hex = "c28fc3acc39f596a0cc2912fc2aa5426c282c29bc2b41bc2ab68c2b716c285c28cc391c29ac3aec3a54ac2aac390c3a6c2a1c3961502c3bb4374c3a8c28ac291c38ac3981bc384c38d"
print(ciphertext_hex) 

ciphertext = bytes.fromhex(ciphertext_hex).decode('utf-8')  # Convert hex string to bytes

# Try timestamps within a reasonable range
time_given = 1697043249.53 # Get current Unix timestamp
time_range = 50 # because of time.sleep(random.randint(0, 50))

for t in range(51): # because of time.sleep(random.randint(0, 50))
    random.seed(t+time_given)  # Set seed to test this timestamp
    decrypted = ""
    for c in ciphertext:
        key = random.randint(0, 255)
        decrypted += chr(key ^ ord(c)) # Reverse XOR
    print(f"Timestamp utilisé : {t}")
    print(f"[i={t}] Flag : ", decrypted)
