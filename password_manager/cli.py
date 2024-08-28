from password_manager.storage.json_file_storage import JSONFileStorage
from password_manager.storage.sqlite_storage import SqliteStorage
from password_manager.storage.ini_file_storage import INIFileStorage
from password_manager.secure_storage import (
    SecureStorage,
    EncryptionError,
    DecryptionError,
)
from password_manager.crypto.key import derive_key
import os


def _print_banner():
    print("\nWelcome to the Password Manager!\n\n")


def _prepare_key() -> bytes:
    # ask for master password
    master_password = input(
        "Please enter the master password: "
    )  # TODO should mask password input
    salt = bytes(
        [i for i in range(16)]
    )  # TODO change this approach to a more secure way. Salt must be related to the password and kept safe
    return derive_key(master_password, salt)


def _prepare_secure_storage() -> SecureStorage:
    base_dir = "data"
    if not (os.path.exists(base_dir) and os.path.isdir(base_dir)):
        os.makedirs(base_dir)

    # data_file_path = os.path.join(base_dir, "data.ini")
    # storage = INIFileStorage(data_file_path)
    # data_file_path = os.path.join(base_dir, "data.json")
    # storage = JSONFileStorage(data_file_path)
    data_file_path = os.path.join(base_dir, "data.db")
    storage = SqliteStorage(data_file_path)

    return SecureStorage(storage)


def _print_help():
    print(
        """
List of available commands:
  put id password
    - Stores a password based associated with the id
  get id
    - Returns a password based on id
  list
    - List all stored ids
  delete id
    - Deletes a password based on id
  help
    - Prints the help
  exit/quit
    - Close the application
"""
    )


def _process_commands(storage: SecureStorage, key: bytes):
    print("Enter the command:")
    while True:
        command = input("> ")

        try:
            match command.split():
                case ["put", id, password]:
                    storage.put(key, id, password)
                    print(f"Stored/Updated password for id '{id}'")
                case ["get", id]:
                    password = storage.get(key, id)
                    if password:
                        print(f"Retrieved: {password}")
                    else:
                        print("Not found")
                case ["list"]:
                    ids = storage.list()
                    ids_string = ", ".join(ids)
                    print(f"Available ids:\n  {ids_string}")
                case ["delete", id]:
                    storage.delete(id)
                    print(f"Deleted password for id '{id}'")
                case ["help"]:
                    _print_help()
                case ["exit"] | ["quit"]:
                    break
                case _:
                    print("Invalid input. Enter 'help' for more information.")
        except EncryptionError as exc:
            print(f"Failed: {exc}")
        except DecryptionError as exc:
            print(f"Failed: {exc}")
        except Exception as exc:
            print(f"Failed: {exc}")


def main():
    """Main entry point of the CLI app"""

    _print_banner()
    _print_help()

    try:
        key = _prepare_key()
        storage = _prepare_secure_storage()

        _process_commands(storage, key)
    except Exception as exc:
        print(f"Error: {exc}")
    except KeyboardInterrupt:
        print("Bye!")


if __name__ == "__main__":
    main()
