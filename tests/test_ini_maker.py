from password_manager.storage.ini_file_storage.ini_maker import make


def test_ini_maker():
    """Test make ini data"""

    expected_text = "k1=v1\nk2=v2\nk3=v3"

    data = {"k1": "v1", "k2": "v2", "k3": "v3"}

    assert make(data) == expected_text


def test_delimiter():
    """Test delimiters"""

    data = {"k1": "v1", "k2": "v2", "k3": "v3"}

    assert make(data) == "k1=v1\nk2=v2\nk3=v3"
    assert make(data, delimiter=":") == "k1:v1\nk2:v2\nk3:v3"
    assert make(data, delimiter="->") == "k1->v1\nk2->v2\nk3->v3"
    assert make(data, delimiter=":", new_line="\r\n") == "k1:v1\r\nk2:v2\r\nk3:v3"
