import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.exceptions import InvalidTag


def encrypt(key: bytes, plain_data: str, delimiter: str = ":") -> str:
    """Encrypts the data and returns a cipher text along with iv and tag as string.

    Args:
        key (bytes): Key used for encryption
        plain_data (str): Plain text data to be encrypted
        delimiter (str, optional): Delimiter that separates iv, tag and cipher text. Defaults to ":".

    Returns:
        str: Encrypted data containing: iv[`delimiter`]cipher_text[`delimiter`]tag
    """
    try:
        iv = os.urandom(16)  # Initialization vector
        cipher = Cipher(algorithms.AES(key), modes.GCM(iv), backend=default_backend())
        encryptor = cipher.encryptor()
        cipher_text = encryptor.update(plain_data.encode()) + encryptor.finalize()
        return delimiter.join([iv.hex(), cipher_text.hex(), encryptor.tag.hex()])
    except ValueError as exc:
        raise DecryptionError(f"Invalid key: {exc}")


def decrypt(key: bytes, encrypted_data: str, delimiter: str = ":") -> str:
    """Decrypts an encrypted data. Encrypted data must be formatted as iv[`delimiter`]cipher_text[`delimiter`]tag

    Args:
        key (bytes): Key used for decryption
        encrypted_data (str): Encrypted data containing: iv[`delimiter`]cipher_text[`delimiter`]tag
        delimiter (str, optional): Delimiter that separates iv, tag and cipher text. Defaults to ":".

    Returns:
        str: Decrypted data as string
    """

    try:
        [iv, cipher_text, tag] = encrypted_data.split(delimiter)
        iv = bytes.fromhex(iv)
        cipher_text = bytes.fromhex(cipher_text)
        tag = bytes.fromhex(tag)
    except ValueError:  # raises when encrypted data is not well formatted
        raise DecryptionError("encrypted_data is not in valid format.")
    try:
        cipher = Cipher(
            algorithms.AES(key), modes.GCM(iv, tag), backend=default_backend()
        )
        decryptor = cipher.decryptor()
        plain_data = decryptor.update(cipher_text) + decryptor.finalize()
        return plain_data.decode()
    except ValueError as exc:
        raise DecryptionError(f"Invalid key: {exc}")
    except InvalidTag:  # raises when key is invalid
        raise DecryptionError("Invalid key or corrupted data.")


class EncryptionError(Exception):
    """Exception to indicate any type of encryption failure"""

    pass


class DecryptionError(Exception):
    """Exception to indicate any type of decryption failure"""

    pass
