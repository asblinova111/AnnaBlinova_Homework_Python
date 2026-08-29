import pytest
from string_utils import StringUtils


@pytest.fixture
def utils():
    return StringUtils()


class TestCapitalize:
    def test_normal_string(self, utils):
        assert utils.capitalize("skypro") == "Skypro"

    def test_empty_string(self, utils):
        assert utils.capitalize("") == ""

    def test_single_letter(self, utils):
        assert utils.capitalize("a") == "A"

    def test_already_capitalized(self, utils):
        assert utils.capitalize("Skypro") == "Skypro"

    def test_all_uppercase(self, utils):
        assert utils.capitalize("SKYPRO") == "Skypro"

    def test_capitalize_none(self, utils):
        assert utils.capitalize(None) == ""


class TestTrim:
    def test_leading_spaces(self, utils):
        assert utils.trim("   skypro") == "skypro"

    def test_no_leading_spaces(self, utils):
        assert utils.trim("skypro") == "skypro"

    def test_only_spaces(self, utils):
        assert utils.trim("   ") == ""

    def test_empty_string(self, utils):
        assert utils.trim("") == ""

    def test_spaces_in_middle_and_end(self, utils):
        # Важно: trim должен удалять только ведущие пробелы
        assert utils.trim("  sky pro ") == "sky pro "

    def test_trim_none(self, utils):
        assert utils.trim(None) == ""

    def test_trim_with_tabs(self, utils):
        assert utils.trim("\t\tskypro") == "skypro"


class TestContains:
    def test_symbol_present(self, utils):
        assert utils.contains("SkyPro", "S") is True

    def test_symbol_absent(self, utils):
        assert utils.contains("SkyPro", "U") is False

    def test_empty_string(self, utils):
        assert utils.contains("", "a") is False

    def test_symbol_longer_than_string(self, utils):
        assert utils.contains("ab", "abc") is False

    def test_case_sensitive(self, utils):
        assert utils.contains("SkyPro", "s") is False

    def test_contains_none_string(self, utils):
        assert utils.contains(None, "a") is False


class TestDeleteSymbol:
    def test_delete_single_char(self, utils):
        assert utils.delete_symbol("SkyPro", "k") == "SyPro"

    def test_delete_substring(self, utils):
        assert utils.delete_symbol("SkyPro", "Pro") == "Sky"

    def test_symbol_not_present(self, utils):
        assert utils.delete_symbol("SkyPro", "X") == "SkyPro"

    def test_delete_all_occurrences(self, utils):
        assert utils.delete_symbol("banana", "a") == "bnn"

    def test_empty_string(self, utils):
        assert utils.delete_symbol("", "a") == ""

    def test_delete_entire_string(self, utils):
        assert utils.delete_symbol("abc", "abc") == ""

    def test_delete_symbol_none_string(self, utils):
        assert utils.delete_symbol(None, "a") == ""
