from typing import Dict


def make(data: Dict[str, str], delimiter: str = "=", new_line: str = "\n") -> str:
    """Makes a INI file format text string based on input dictionary.

    Args:
        data (Dict[str, str]): Input data in dictionary form
        delimiter (str, optional): Delimiter character. Defaults to "=".
        new_line (str, optional): New line character. Defaults to "\n".

    Returns:
        str: A line separated string in INI format
    """

    content = ""

    for k, v in data.items():
        content += k.strip() + delimiter + v.strip() + new_line

    return content.strip()
