import os


def read_entire_file(file_path: str) -> str:
    """Reads the entire text file and return content as string

    Args:
        file_path (str): Path of the text file

    Returns:
        str: The entire file as string
    """

    # return empty string if file not exists
    if not os.path.exists(file_path):
        return ""

    with open(file_path, "rt") as file:
        content = file.read()

    return content


def write_entire_file(file_path: str, content: str) -> None:
    """Writes text into the file and replaces the file content. Creates the file if not exists.

    Args:
        file_path (str): _description_
        content (str): _description_
    """

    with open(file_path, "+wt") as file:
        file.write(content)
