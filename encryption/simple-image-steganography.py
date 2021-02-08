'''
Simple way to hide message in image

Requires cryptosteganography and python version 3.8:
https://github.com/computationalcore/cryptosteganography

'''

from cryptosteganography import CryptoSteganography

# generate a key and store it in file named s.key
key = Fernet.generate_key()
with open("s.key", "wb") as keyfile:
	keyfile.write(key)

# to open s.key once stored
# return open("s.key", "rb").read()