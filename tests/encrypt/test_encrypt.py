import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    assert encrypt_message("hello world", -2) == "dlrow olleh"
    assert encrypt_message("hello world", 2) == "dlrow oll_eh"
    assert encrypt_message("hello world", 3) == "leh_dlrow ol"

    with pytest.raises(TypeError):
        encrypt_message("hello world", "2")
