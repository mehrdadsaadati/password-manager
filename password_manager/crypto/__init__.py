import os
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes


# Key derivation example with PBKDF2
def derive_key(master_password, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend(),
    )
    key = kdf.derive(master_password.encode())
    return key


# Encrypting a password
def encrypt_password(key, plaintext_password):
    iv = os.urandom(16)  # Initialization vector
    cipher = Cipher(algorithms.AES(key), modes.GCM(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext_password.encode()) + encryptor.finalize()
    return iv, ciphertext, encryptor.tag


# Decrypting a password
def decrypt_password(key, iv, ciphertext, tag):
    cipher = Cipher(algorithms.AES(key), modes.GCM(iv, tag), backend=default_backend())
    decryptor = cipher.decryptor()
    plaintext_password = decryptor.update(ciphertext) + decryptor.finalize()
    return plaintext_password.decode()


# Usage
master_password = "your_master_password"
salt = os.urandom(16)
key = derive_key(master_password, salt)

# Encrypt
iv, ciphertext, tag = encrypt_password(key, "my_secret_password")

# Decrypt
decrypted_password = decrypt_password(key, iv, ciphertext, tag)
print(decrypted_password)  # Output: 'my_secret_password'
