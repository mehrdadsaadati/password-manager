from password_manager.secure_storage import (
    SecureStorage,
    EncryptionError,
    DecryptionError,
)
from password_manager.storage.in_memory_storage import InMemoryStorage

import pytest


def test_secure_storage():
    """Test secure storage using in memory storage"""

    key = bytes([i for i in range(32)])

    storage = SecureStorage(InMemoryStorage())

    # put one item
    storage.put(key, "1", "p1")
    # test get
    assert storage.get(key, "1") == "p1"

    # put more items
    storage.put(key, "2", "p2")
    storage.put(key, "3", "p3")
    storage.put(key, "4", "p4")
    storage.put(key, "5", "p5")
    # list
    assert storage.list() == ["1", "2", "3", "4", "5"]

    # put duplicated key (expect no error, data should be updated)
    storage.put(key, "4", "p4_2")
    assert storage.get(key, "4") == "p4_2"

    # delete an item
    storage.delete("5")
    # check deletion
    assert storage.list() == ["1", "2", "3", "4"]

    # get deleted item
    assert storage.get(key, "5") is None

    # test invalid key
    with pytest.raises(EncryptionError):
        storage.put(bytes([1, 2, 3]), "x", "X")
    with pytest.raises(DecryptionError):
        storage.get(bytes([1, 2, 3]), "1")

    # put empty item
    storage.put(key, "e", "")
    # test get
    assert storage.get(key, "e") == ""
