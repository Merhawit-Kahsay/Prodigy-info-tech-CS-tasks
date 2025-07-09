from PIL import Image
# Load the image
image = Image.open("C:\\Users\\hp\\Desktop\\Prodigy info tech tasks\\PRODIGY_CS_02\\to be_encrypted.jpeg")

# Get the image dimensions
width, height = image.size

# Define the encryption key (a simple example)
key = 0x12345678

# Iterate over each pixel in the image
for x in range(width):
    for y in range(height):
        # Get the pixel value (RGB)
        pixel = image.getpixel((x, y))

        # Encrypt the pixel value using XOR
        encrypted_pixel = (
            pixel[0] ^ (key & 0xFF),
            pixel[1] ^ ((key >> 8) & 0xFF),
            pixel[2] ^ ((key >> 16) & 0xFF)
        )

        # Set the encrypted pixel value
        image.putpixel((x, y), encrypted_pixel)

# Save the encrypted image
image.save("C:\\Users\\hp\\Desktop\\Prodigy info tech tasks\\PRODIGY_CS_02\\encrypted.jpeg")