from password_manager.crypto.key import derive_key, random_salt


def test_salt_format():
    """Test if salt is bytes and len is 16"""

    salt = random_salt()

    assert type(salt) is bytes
    assert len(salt) == 16


def test_salt_randomness():
    """Test salt is randomly generated and not repeated"""

    salts = []
    # this is not an exact randomness test.
    # We just want to make sure a predefined salt is not returned.
    # So, 10 iteration is really enough
    for i in range(10):
        salt = random_salt()
        assert salt not in salts
        salts.append(salt)


def test_key_format():
    """Test created key is a bytes data in specified format"""

    master_password = "Simple master password!"
    salt = random_salt()
    key = derive_key(master_password, salt, key_len=8)
    assert type(key) is bytes
    assert len(key) == 8
    key = derive_key(master_password, salt, key_len=16)
    assert type(key) is bytes
    assert len(key) == 16
    key = derive_key(master_password, salt, key_len=32)
    assert type(key) is bytes
    assert len(key) == 32


def test_iteration_effect():
    """Test iteration parameter changes the results"""

    master_password = "Simple master password!"
    salt = random_salt()
    key1 = derive_key(master_password, salt, iterations=1000)
    key2 = derive_key(master_password, salt, iterations=20000)

    assert key1 != key2, "iteration parameter has no effect"


def test_salt_effect():
    """Test salt parameter changes the results"""

    master_password = "Simple master password!"
    salt1 = random_salt()
    key1 = derive_key(master_password, salt1)
    salt2 = random_salt()
    key2 = derive_key(master_password, salt2)

    assert key1 != key2, "salt parameter has no effect"


def test_repeated_generation():
    """Test if the same key is always generated using the same salt and iteration"""

    master_password = "Simple master password!"
    salt = random_salt()
    iteration = 100000

    key = derive_key(master_password, salt, iteration)
    for i in range(10):
        new_key = derive_key(master_password, salt, iteration)
        assert key == new_key, "Key changes on each generation request"
        key = new_key
