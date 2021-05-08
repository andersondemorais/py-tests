import pytest
from functions import ssum


@pytest.fixture
def word():
    return "python"


def test_uppercase(word):
    assert word.upper() == "PYTHON"


def test_convert_to_int(word):
    with pytest.raises(ValueError):
        int(word) == 0


def test_functions():
    assert ssum(4) == 8
    assert ssum("33") == 37
    assert ssum("a3i") == 0
