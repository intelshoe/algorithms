'''
Simple way to hide message in image

Requires cryptography module, cryptosteganography and python version 3.8:
https://github.com/computationalcore/cryptosteganography

'''
from cryptography.fernet import Fernet 
from cryptosteganography import CryptoSteganography

# generate a key and store it in file named s.key
key = Fernet.generate_key()
with open("s.key", "wb") as keyfile:
	keyfile.write(key)

# secret message to store in image
msg = "The secret word is gravy!".encode()

# encrypt
f = Fernet(key)
emsg = f.encrypt(msg)
print(emsg)

# to open s.key once stored
# return open("s.key", "rb").read()