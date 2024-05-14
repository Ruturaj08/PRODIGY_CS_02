from PIL import Image

def encrypt_image(image_path, key):
    img = Image.open(image_path)
    width, height = img.size
    encrypted_img = Image.new("RGB", (width, height))

    for y in range(height):
        for x in range(width):
            r, g, b = img.getpixel((x, y))
            r = (r + key) % 256
            g = (g + key) % 256
            b = (b + key) % 256
            encrypted_img.putpixel((x, y), (r, g, b))

    encrypted_img.save("encrypted_image.png")
    print("Image encrypted successfully!")

def decrypt_image(image_path, key):
    img = Image.open(image_path)
    width, height = img.size
    decrypted_img = Image.new("RGB", (width, height))

    for y in range(height):
        for x in range(width):
            r, g, b = img.getpixel((x, y))
            r = (r - key) % 256
            g = (g - key) % 256
            b = (b - key) % 256
            decrypted_img.putpixel((x, y), (r, g, b))

    decrypted_img.save("decrypted_image.png")
    print("Image decrypted successfully!")

def main():
    image_path = input("Enter the path to the image file: ")
    key = int(input("Enter the encryption/decryption key: "))

    choice = input("Enter 'E' for encryption or 'D' for decryption: ").upper()
    if choice == 'E':
        encrypt_image(image_path, key)
    elif choice == 'D':
        decrypt_image(image_path, key)
    else:
        print("Invalid choice. Please enter 'E' or 'D'.")

if __name__ == "__main__":
    main()