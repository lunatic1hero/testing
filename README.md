def decode_image_msb(image_path):
    from PIL import Image
    img = Image.open(image_path)
    binary_secret_data = ''
    for pixel in list(img.getdata()):
        r, g, b = pixel
        binary_secret_data += str((r & 0b10000000) >> 7)
        binary_secret_data += str((g & 0b10000000) >> 7)
        binary_secret_data += str((b & 0b10000000) >> 7)

    # Convert binary data to string
    secret_data = ''
    for i in range(0, len(binary_secret_data), 8):
        byte = binary_secret_data[i:i+8]
        secret_data += chr(int(byte, 2))

    return secret_data

# Usage
decoded_message = decode_image_msb(r'C:\Users\Birad\Downloads\Ninja-and-Prince-Genji-Ukiyoe-Utagawa-Kunisada.flag.png')
print("Decoded message:", decoded_message)
