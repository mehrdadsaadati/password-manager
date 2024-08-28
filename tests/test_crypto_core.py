from password_manager.crypto.core import encrypt, decrypt, DecryptionError
import pytest


def test_cryptography():
    """Test encrypted and decrypted contents are interchangeable"""

    key = bytes([i for i in range(32)])
    original_data = "  This is a plain message to be encrypted!  "

    enc = encrypt(key, original_data)
    assert enc != original_data
    assert decrypt(key, enc) == original_data

    # check invalid key for decryption
    invalid_key = bytes([i + 1 for i in range(32)])
    with pytest.raises(DecryptionError):
        decrypt(invalid_key, enc)

    # check invalid input format
    with pytest.raises(DecryptionError):
        decrypt(key, "")

    # check invalid key size
    with pytest.raises(DecryptionError):
        decrypt(bytes([1, 2, 3]), enc)

    # check invalid key size
    with pytest.raises(DecryptionError):
        encrypt(bytes([1, 2, 3]), original_data)

    # empty input encryption
    enc = encrypt(key, "")
    assert decrypt(key, enc) == ""
