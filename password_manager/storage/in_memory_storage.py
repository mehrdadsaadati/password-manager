from password_manager.storage import Storage
from typing import List


class InMemoryStorage(Storage):
    """In memory data storage.

    Data is stored in memory for the life of the application. Nothing is permanently stored.
    """

    def __init__(self) -> None:
        super().__init__()
        self.__data = {}  # The memory storage (dictionary)

    def put(self, id: str, password: str) -> None:
        """Store a password in database

        Args:
            id (str): Id of the entity
            password (str): The plain password
        """

        self.__data[id] = password

    def get(self, id: str) -> str | None:
        """Gets the password based on Id

        Args:
            id (str): Id of the entity

        Returns:
            str | None: The password string if found, otherwise None is returned
        """

        if id in self.__data:
            return self.__data[id]

        return None

    def list(self) -> List[str]:
        """Returns the list of stored entities (Only Ids are returned)

        Returns:
            List[str]: List of stored entity ids
        """

        return list(self.__data.keys())

    def delete(self, id: str) -> None:
        """Deletes an entity.

        Args:
            id (str): Id of the entity
        """

        if id in self.__data:
            del self.__data[id]
