from password_manager.storage import Storage
from password_manager.storage.utils import read_entire_file, write_entire_file
from typing import List
import json


class JSONFileStorage(Storage):
    """JSON File data storage.

    Data is stored in JSON file.
    """

    def __init__(self, file_path: str) -> None:
        """Initialize the JSON file storage.

        Args:
            file_path (str): Path of the database. Extension of .json is recommended.
        """

        super().__init__()

        # read current data from the database file
        data = read_entire_file(file_path)
        # store a copy of parsed data in memory for faster lookups
        self.__data = json.loads(data or "{}")
        self.file_path = file_path

    def put(self, id: str, password: str) -> None:
        """Store a password in database

        Args:
            id (str): Id of the entity
            password (str): The plain password
        """

        # update in memory data
        self.__data[id] = password

        # update data in the file
        self.__store_changes()

    def get(self, id: str) -> str | None:
        """Gets the password based on Id

        Args:
            id (str): Id of the entity

        Returns:
            str | None: The password string if found, otherwise None is returned
        """

        # no need to lookup for data in the file as we have already read the file in the beginning
        if id in self.__data:
            return self.__data[id]

        return None

    def list(self) -> List[str]:
        """Returns the list of stored entities (Only Ids are returned)

        Returns:
            List[str]: List of stored entity ids
        """

        # no need to lookup for data in the file as we have already read the file in the beginning
        return list(self.__data.keys())

    def delete(self, id: str) -> None:
        """Deletes an entity.

        Args:
            id (str): Id of the entity
        """

        # update data in memory
        if id in self.__data:
            del self.__data[id]

        # update data in the file
        self.__store_changes()

    def __store_changes(self):
        """Stores the in memory data into the file"""

        # create ini text from updated data
        text = json.dumps(self.__data)
        # write new data to the file
        write_entire_file(self.file_path, text)
