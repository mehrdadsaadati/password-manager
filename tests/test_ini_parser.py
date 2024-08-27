from password_manager.storage.ini_file_storage.ini_parser import parse


def test_ini_text_parse():
    """Test parse method"""

    text = """
k1=v1
k2 = v2

k3 = v3  
 k4  = a=b=c
bad_content

"""
    assert parse(text) == {"k1": "v1", "k2": "v2", "k3": "v3", "k4": "a=b=c"}


def test_delimiter():
    """Test using different delimiters"""

    text = """
k1 : v1
k2 = v2
k3 -> v3
"""
    assert parse(text, delimiter=":") == {"k1": "v1"}
    assert parse(text) == {"k2": "v2"}
    assert parse(text, delimiter="->") == {"k3": "v3"}
