'''
Simple way to encrypt and decrypt an image

'''
import sys

# take in path to image from command line argument
image_location = sys.argv[1]

print("Looking for test.png in home directory.")
# opening the file with option rb allows reading binary data
fo = open(image_location, "rb")
image = fo.read()
fo.close()

print("")
print("The secret key is 12.")
image = bytearray(image)
key = 12

for index, value in enumerate(image):
   # ^ means bitwise exclusive XOR
   image[index] = value^key

print("")
print("Image encrypted. Saving file as etest.png")
fo = open("etest.png", "wb")
fo.write(image)
fo.close()

image = bytearray(image)

for index, value in enumerate(image):
   # ^ means bitwise exclusive XOR
   image[index] = key^value

fo = open("dtest.png", "wb")
fo.write(image)
fo.close()
print("")
print("The images is decrypted and saved as dtest.png")
