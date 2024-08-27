from password_manager.storage import Storage
import sqlite3
from typing import List


class SqliteStorage(Storage):
    """Sqlite data storage.

    Data is stored in an Sqlite database.
    """

    def __init__(self, file_path: str) -> None:
        """Initialize the Sqlite storage.

        Args:
            file_path (str): Path of the database. Extension of .db is recommended.
        """

        super().__init__()
        self.conn = sqlite3.connect(file_path)
        self.__create_tables()

    def __create_tables(self) -> None:
        """Create table for database"""

        with self.conn:
            self.conn.execute(
                """
CREATE TABLE IF NOT EXISTS passwords (
    id TEXT PRIMARY KEY,
    password TEXT NOT NULL
)
"""
            )

    def put(self, id: str, password: str) -> None:
        """Store a password in database

        Args:
            id (str): Id of the entity
            password (str): The plain password
        """

        with self.conn:
            cursor = self.conn.execute(
                "SELECT id, password FROM passwords WHERE id=?", (id,)
            )
            exist = cursor.fetchone()

            if exist:
                self.conn.execute(
                    "UPDATE passwords SET password=? WHERE id=?", (password, id)
                )
            else:
                self.conn.execute(
                    "INSERT INTO passwords (id, password) VALUES(?, ?)", (id, password)
                )

    def get(self, id: str) -> str | None:
        """Gets the password based on Id

        Args:
            id (str): Id of the entity

        Returns:
            str | None: The password string if found, otherwise None is returned
        """

        with self.conn:
            cursor = self.conn.execute(
                "SELECT id, password FROM passwords WHERE id=?", (id,)
            )
            item = cursor.fetchone()

            return item[1] if item else None

    def list(self) -> List[str]:
        """Returns the list of stored entities (Only Ids are returned)

        Returns:
            List[str]: List of stored entity ids
        """

        with self.conn:
            cursor = self.conn.execute("SELECT id, password FROM passwords")
            return [row[0] for row in cursor.fetchall()]

    def delete(self, id: str) -> None:
        """Deletes an entity.

        Args:
            id (str): Id of the entity
        """

        with self.conn:
            self.conn.execute("DELETE FROM passwords WHERE id=?", (id,))
