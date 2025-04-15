def hexdump_encode_1(message, image):
    # Hiding text in hex dump
    # encode message as binary then append result to image file
    with open(image, "ab") as f:
        f.write(message.encode('utf8'))

def hexdump_encode_2(message, image):
    with open(image, "ab") as cover, open("secret.txt", "rb") as secret:
        cover.write(secret.read())



text = "Hello World!"
picture = "plain_image.jpg"
hexdump_encode_2(text, picture)