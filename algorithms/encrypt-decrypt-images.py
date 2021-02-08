'''
Simple way to encrypt and decrypt an image

'''

print("Looking for test.png in home directory.")
# opening the file with option rb allows reading binary data
fo = open("\test.png", "rb")
image = fo.read()
fo.close()

print("/n")
print("The secret key is 12.")
image = bytearray(image)
key = 12

for index, value in enumerate(image):
   image[index] = value^key

print("/n")
print("Image encrypted. Saving file as etest.png")
fo = open("\etest.png", "wb")
fo.write(image)
fo.close()

image = bytearray(image)

for index, value in enumerate(image):
   image[index] = key^value

fo = open("\dtest.png", "wb")
fo.write(image)
fo.close()
print("/n")
print("The images is decrypted and saved as dtest.png")
