import pytest
from string_utils import StringUtils

utils = StringUtils()

@pytest.mark.positive
@pytest.mark.parametrize("string, expected", [
    ("hello", "Hello"),
    ("hello world", "Hello world"),
    (" after space", " after space")
])
def test_capitalize_positive(string, expected):
    assert utils.capitalize(string) == expected

@pytest.mark.negative
@pytest.mark.parametrize("string, expected", [
    ("", ""),
    ("  ", "  "),
    ("1234a", "1234a")
])
def test_capitalize_negative(string, expected):
    assert utils.capitalize(string) == expected

@pytest.mark.positive
@pytest.mark.parametrize("string, expected", [
    (" Hello", "Hello"),
    (" 1234", "1234"),
    ("   Hello", "Hello"),
    (" Hello world", "Hello world")
])
def test_trim_positive(string, expected):
    assert utils.trim(string) == expected

@pytest.mark.negative
@pytest.mark.parametrize("string, expected", [
    ("Hello", "Hello"),
    ("hello world", "hello world"),
    ("  ", ""),
    ("", "")
])
def test_trim_negative(string, expected):
    assert utils.trim(string) == expected

@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("Hello", "o", True),
    ("SkyPro", "P", True),
    ("Hello world", "w", True),
    ("SkyPro", "Pro", True),
    ("123Example", "3", True),
    (" ", " ", True),
    ("Hello world", " ", True)
])
def test_contains_positive(string, symbol, expected):
    assert utils.contains(string, symbol) == expected

@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("Hello", "x", False),
    ("Hello", "h", False),
    ("SkyPro", "Prof", False),
    ("", "x", False),
])
def test_contains_negative(string, symbol, expected):
    assert utils.contains(string, symbol) == expected

@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("Hello", "o", "Hell"),
    ("Hello world", " world", "Hello"),
    ("Engineer", "e", "Enginr")
])
def test_delete_positive(string, symbol, expected):
    assert utils.delete_symbol(string, symbol) == expected

@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("Hello", "a", "Hello"),
    ("SkyPro", "s", "SkyPro"),
    ("", "a", ""),
    ("", "", "")
])
def test_delete_negative(string, symbol, expected):
    assert utils.delete_symbol(string, symbol) == expected