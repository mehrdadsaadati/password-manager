from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
import os


def derive_key(
    master_password: str, salt: bytes, iterations: int = 100000, key_len: int = 32
) -> bytes:
    """Derives a key from master password using PBKDF2

    Args:
        master_password (str): Master password
        salt (bytes): Salt used in key derivation
        iterations (int): Number of iterations
        key_len (int): Length of the generated key (in bytes)

    Returns:
        bytes: Derived key
    """

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=key_len,
        salt=salt,
        iterations=iterations,
        backend=default_backend(),
    )
    key = kdf.derive(master_password.encode())
    return key


def random_salt() -> bytes:
    """Generates a 16 bytes secure random salt

    Returns:
        bytes: A 16 bytes secure random salt
    """

    return os.urandom(16)
