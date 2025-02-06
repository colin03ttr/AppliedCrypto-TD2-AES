import random
import time

flag="REDACTED"

print(time.time())
#1697043249.53

time.sleep(random.randint(0, 50))
random.seed(time.time())

ct=""
for c in flag:
    ct += c.hr(random.randint(0,255) ^ ord(c)) # remove the dots in c.hr (it's chr)

print(ct.encode().hex())
#c28fc3acc39f596a0cc2912fc2aa5426c282c29bc2b41bc2ab68c2b716c285c28cc391c29ac3aec3a54ac2aac390c3a6c2a1c3961502c3bb4374c3a8c28ac291c38ac3981bc384c38d