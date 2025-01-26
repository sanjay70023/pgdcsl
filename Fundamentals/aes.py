from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os

# Generate a random key and IV
def generate_key_iv():
    key = os.urandom(32)  # 256-bit key for AES
    iv = os.urandom(16)   # 128-bit IV
    return key, iv

# Encrypt the file
def encrypt_file(input_file, output_file, key, iv):
    with open(input_file, 'rb') as f:
        data = f.read()

    # Add padding
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(data) + padder.finalize()

    # Encrypt data
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

    # Save encrypted data to file
    with open(output_file, 'wb') as f:
        f.write(iv + encrypted_data)

    print(f"File encrypted and saved as {output_file}")

# Decrypt the file
def decrypt_file(input_file, output_file, key):
    with open(input_file, 'rb') as f:
        iv = f.read(16)  # Read IV
        encrypted_data = f.read()

    # Decrypt data
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    padded_data = decryptor.update(encrypted_data) + decryptor.finalize()

    # Remove padding
    unpadder = padding.PKCS7(128).unpadder()
    data = unpadder.update(padded_data) + unpadder.finalize()

    # Save decrypted data to file
    with open(output_file, 'wb') as f:
        f.write(data)

    print(f"File decrypted and saved as {output_file}")

# Example usage
key, iv = generate_key_iv()

# Input and output files
input_file = 'plaintext.txt'
encrypted_file = 'encrypted.txt'
decrypted_file = 'decrypted.txt'

# Encrypt the file
encrypt_file(input_file, encrypted_file, key, iv)

# Decrypt the file
decrypt_file(encrypted_file, decrypted_file, key)
