with open("C:\\Users\\hp\\Desktop\\Prodigy info tech tasks\\task 4\\encrypted.jpeg", "rb") as file:
    image = file.read()
#file.close()

image = bytearray(image)

key = 48

for i in range(len(image)):
    image[i] = image[i] ^ key  # Use XOR operation for encryption

with open("C:\\Users\\hp\\Desktop\\Prodigy info tech tasks\\task 4\\to be_encrypted.jpeg", "wb") as file:
    file.write(image)