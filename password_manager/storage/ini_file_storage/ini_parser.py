from typing import Dict


def parse(text: str, delimiter: str = "=") -> Dict[str, str]:
    """Parses a text input string as INI format and returns the key value pairs as a dictionary.

    Args:
        text (str): Input text string in INI format
        delimiter (str, optional): Delimiter used to separate key value pairs. Defaults to '='.

    Returns:
        Dict[str, str]: Dictionary containing all key value pairs
    """

    data = {}
    lines = text.splitlines()
    for line in lines:
        # extract well formatted lines and ignore the rest
        match line.split(delimiter, maxsplit=1):
            case [key, val]:
                data[key.strip()] = val.strip()

    return data
