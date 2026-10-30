import pytest
from string_utils import StringUtils


@pytest.fixture
def utils():
    return StringUtils()


class TestCapitalize:

    @pytest.mark.parametrize("string, expected", [
        ("skypro", "Skypro"),
        ("", ""),
        ("a", "A"),
        ("Skypro", "Skypro"),
        ("SKYPRO", "Skypro"),
    ])
    def test_capitalize_positive(self, utils, string, expected):
        assert utils.capitalize(string) == expected

    def test_capitalize_none(self, utils):
        with pytest.raises(AttributeError):
            utils.capitalize(None)


class TestTrim:

    @pytest.mark.parametrize("string, expected", [
        ("   skypro", "skypro"),
        ("skypro", "skypro"),
        ("   ", ""),
        ("", ""),
        ("  sky pro ", "sky pro "),
    ])
    def test_trim_positive(self, utils, string, expected):
        assert utils.trim(string) == expected

    def test_trim_none(self, utils):
        with pytest.raises(AttributeError):
            utils.trim(None)

    def test_trim_with_tabs(self, utils):
        # Этот тест упадет на оригинальном коде (DEF-001)
        assert utils.trim("\t\tskypro") == "skypro"


class TestContains:

    @pytest.mark.parametrize("string, symbol, expected", [
        ("SkyPro", "S", True),
        ("SkyPro", "U", False),
        ("", "a", False),
        ("ab", "abc", False),
        ("SkyPro", "s", False),
        ("SkyPro", "", True),
    ])
    def test_contains_positive(self, utils, string, symbol, expected):
        assert utils.contains(string, symbol) == expected

    def test_contains_none_string(self, utils):
        assert utils.contains(None, "a") is False


class TestDeleteSymbol:

    @pytest.mark.parametrize("string, symbol, expected", [
        ("SkyPro", "k", "SyPro"),
        ("SkyPro", "Pro", "Sky"),
        ("SkyPro", "X", "SkyPro"),
        ("banana", "a", "bnn"),
        ("", "a", ""),
        ("abc", "abc", ""),
    ])
    def test_delete_symbol_positive(self, utils, string, symbol, expected):
        assert utils.delete_symbol(string, symbol) == expected

    def test_delete_symbol_none_string(self, utils):
        assert utils.delete_symbol(None, "a") == ""
