# extracting text from hex dump
def hexdump_extract_1(image: str):
    with open(image, "rb") as f:
        for chunk in iter(lambda: f.read(8), b''):
            print(chunk.decode('utf-8', errors="ignore"), end="")

def hexdump_extract_2(image: str):
    trailer = 'ffd9' # JPEG trailer

    # Get trailer offset
    with open(image, "rb") as cover_secret:
        file = cover_secret.read()
        offset = file.index(bytes.fromhex(trailer))

    # Write cover bytes to output file from offset + trailer length
    with open(image, "rb") as cover_secret, open("secret.txt", "wb") as secret:
        cover_secret.seek(offset + len(trailer)//2)
        secret.write(cover_secret.read())

picture = "plain_image.jpg"
hexdump_extract_2(picture)