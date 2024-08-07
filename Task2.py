# image_encryption_tool.py

import numpy as np
from PIL import Image

def encrypt_image(image_path, operation, key):
    """
    Encrypt an image using pixel manipulation.

    Args:
        image_path (str): Path to the image file.
        operation (str): Operation to perform on each pixel (e.g. "swap", "add", "multiply").
        key (int): Key value for the operation.

    Returns:
        Encrypted image as a PIL Image object.
    """
    image = Image.open(image_path)
    pixels = np.array(image)

    if operation == "swap":
        # Swap pixel values
        pixels[:, :, 0], pixels[:, :, 1] = pixels[:, :, 1], pixels[:, :, 0]
    elif operation == "add":
        # Add key value to each pixel
        pixels += key
        pixels = np.clip(pixels, 0, 255)  # Ensure pixel values are within 0-255 range
    elif operation == "multiply":
        # Multiply each pixel by key value
        pixels *= key
        pixels = np.clip(pixels, 0, 255)  # Ensure pixel values are within 0-255 range
    else:
        raise ValueError("Invalid operation")

    encrypted_image = Image.fromarray(pixels.astype(np.uint8))
    return encrypted_image

def decrypt_image(encrypted_image, operation, key):
    """
    Decrypt an encrypted image using pixel manipulation.

    Args:
        encrypted_image (PIL Image object): Encrypted image.
        operation (str): Operation to reverse (e.g. "swap", "add", "multiply").
        key (int): Key value for the operation.

    Returns:
        Decrypted image as a PIL Image object.
    """
    pixels = np.array(encrypted_image)

    if operation == "swap":
        # Swap pixel values back
        pixels[:, :, 0], pixels[:, :, 1] = pixels[:, :, 1], pixels[:, :, 0]
    elif operation == "add":
        # Subtract key value from each pixel
        pixels -= key
        pixels = np.clip(pixels, 0, 255)  # Ensure pixel values are within 0-255 range
    elif operation == "multiply":
        # Divide each pixel by key value
        pixels //= key
        pixels = np.clip(pixels, 0, 255)  # Ensure pixel values are within 0-255 range
    else:
        raise ValueError("Invalid operation")

    decrypted_image = Image.fromarray(pixels.astype(np.uint8))
    return decrypted_image

def main():
    image_path = input("Enter image path: ")
    operation = input("Enter operation (swap, add, multiply): ")
    key = int(input("Enter key value: "))

    encrypted_image = encrypt_image(image_path, operation, key)
    encrypted_image.save("encrypted_image.png")

    print("Encrypted image saved as encrypted_image.png")

    decrypted_image = decrypt_image(encrypted_image, operation, key)
    decrypted_image.save("decrypted_image.png")

    print("Decrypted image saved as decrypted_image.png")

if __name__ == "__main__":
    main()