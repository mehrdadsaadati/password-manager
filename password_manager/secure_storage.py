from password_manager.crypto import encrypt, decrypt, EncryptionError, DecryptionError
from password_manager.storage import Storage
from typing import List


class SecureStorage:
    def __init__(self, storage: Storage) -> None:
        self.storage = storage

    def put(self, key: bytes, id: str, password: str) -> None:
        """Encrypts and stores a password in database

        Args:
            key (bytes): The cryptography key
            id (str): Id of the entity
            password (str): The plain password
        """

        return self.storage.put(id, encrypt(key, password))

    def get(self, key: bytes, id: str) -> str | None:
        """Retrieves and decrypts the password based on Id

        Args:
            key (bytes): The cryptography key
            id (str): Id of the entity

        Returns:
            str | None: The password string if found, otherwise None is returned
        """

        encrypted = self.storage.get(id)
        if encrypted:
            return decrypt(key, encrypted)
        return None

    def list(self) -> List[str]:
        """Returns the list of stored entities (Only Ids are returned)

        Returns:
            List[str]: List of stored entity ids
        """

        return self.storage.list()

    def delete(self, id: str) -> None:
        """Deletes an entity.

        Args:
            id (str): Id of the entity
        """

        return self.storage.delete(id)
