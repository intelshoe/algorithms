'''
Simple way to hide message in image

Requires cryptography module, cryptosteganography, and python version 3.8:
https://github.com/computationalcore/cryptosteganography

'''
from cryptography.fernet import Fernet 
from cryptosteganography import CryptoSteganography
import sys

# generate a key and store it in file named s.key
key = Fernet.generate_key()
with open("s.key", "wb") as keyfile:
	keyfile.write(key)

# secret message to store in image
# filename from commandline
file = sys.argv[1]
# write msg to msg var
with open(file, "rb") as file:
	msg = file.read()

print(f"{msg}\n\n")
	
# encrypt msg
f = Fernet(key)
emsg = f.encrypt(msg)
print(emsg)

# to decrypt the msg
dmsg = f.decrypt(emsg)
with open("dmsg.txt", "xb") as file:
	file.write(dmsg)

# Hide the msg in the image
hide_msg = CryptoSteganography(key)