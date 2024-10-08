from password_manager.storage.in_memory_storage import InMemoryStorage
from password_manager.storage.ini_file_storage import INIFileStorage
from password_manager.storage.json_file_storage import JSONFileStorage
from password_manager.storage.sqlite_storage import SqliteStorage
import os


def _test_storage(storage):
    """Read write operations on the storage"""

    # put one item
    storage.put("1", "p1")
    # test get
    assert storage.get("1") == "p1"

    # put more items
    storage.put("2", "p2")
    storage.put("3", "p3")
    storage.put("4", "p4")
    storage.put("5", "p5")
    # list
    assert storage.list() == ["1", "2", "3", "4", "5"]

    # put duplicated key (expect no error, data should be updated)
    storage.put("4", "p4_2")
    assert storage.get("4") == "p4_2"

    # delete an item
    storage.delete("5")
    # check deletion
    assert storage.list() == ["1", "2", "3", "4"]

    # get deleted item
    assert storage.get("5") is None


def test_in_memory_storage():
    """Test put, get, list and delete on the in memory storage"""

    storage = InMemoryStorage()

    _test_storage(storage)


def test_ini_file_storage(tmp_path):
    """Test put, get, list and delete on the INI file storage"""

    file_path = os.path.join(tmp_path, "ini_file_storage.ini")

    storage = INIFileStorage(file_path)

    _test_storage(storage)


def test_json_file_storage(tmp_path):
    """Test put, get, list and delete on the JSON file storage"""

    file_path = os.path.join(tmp_path, "json_file_storage.json")

    storage = JSONFileStorage(file_path)

    _test_storage(storage)


def test_sqlite_storage(tmp_path):
    """Test put, get, list and delete on the Sqlite storage"""

    file_path = os.path.join(tmp_path, "sqlite_storage.db")

    storage = SqliteStorage(file_path)

    _test_storage(storage)
