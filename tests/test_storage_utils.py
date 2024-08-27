from password_manager.storage.utils import read_entire_file, write_entire_file
import os


def test_file_read_write(tmp_path):
    """Test utils file read and write operations"""

    content = """
This is a
 multiline
 
 text file.
"""

    # read a non existing file as empty string
    assert read_entire_file(os.path.join(tmp_path, "non_existing_file.txt")) == ""

    # write content to a file
    test_file = os.path.join(tmp_path, "test_file.txt")
    write_entire_file(test_file, content)

    # read the same content from file
    assert read_entire_file(test_file) == content

    # replace content of existing file
    new_content = "New Test Content"
    write_entire_file(test_file, new_content)

    # read the new content from file
    assert read_entire_file(test_file) == new_content
