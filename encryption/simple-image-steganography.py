'''
Simple way to hide message in image

Using cryptography module, cryptosteganography, and python version 3.8:
https://github.com/computationalcore/cryptosteganography
Please note this is pretty insecure.
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
key2 = "Password"
hidden_key = CryptoSteganography(key2)
orig_img = "test.png"
img_out = "hidden_msg_in_img.png"
hidden_key.hide(orig_img, img_out, msg)

# reveal the hidden msg
hidden_msg = hidden_key.retrieve(img_out)
print(f"The image contains this text: \n{hidden_msg}")
