from abc import ABC, abstractmethod
from typing import List


class Storage(ABC):
    """Base class of Storage

    Helps store and retrieve passwords
    """

    @abstractmethod
    def put(self, id: str, password: str) -> None:
        """Store a password in database

        Args:
            id (str): Id of the entity
            password (str): The plain password
        """

        raise NotImplementedError("Not implemented")

    @abstractmethod
    def get(self, id: str) -> str | None:
        """Gets the password based on Id

        Args:
            id (str): Id of the entity

        Returns:
            str | None: The password string if found, otherwise None is returned
        """

        raise NotImplementedError("Not implemented")

    @abstractmethod
    def list(self) -> List[str]:
        """Returns the list of stored entities (Only Ids are returned)

        Returns:
            List[str]: List of stored entity ids
        """

        raise NotImplementedError("Not implemented")

    @abstractmethod
    def delete(self, id: str) -> None:
        """Deletes an entity.

        Args:
            id (str): Id of the entity
        """

        raise NotImplementedError("Not implemented")
