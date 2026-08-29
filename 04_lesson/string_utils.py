
class StringUtils:
    """
    Класс с полезными утилитами для обработки и анализа строк
    """

    def capitalize(self, string: str) -> str:
        """
        Принимает на вход текст, делает первую букву заглавной
        и возвращает этот же текст
        Пример: `capitilize("skypro") -> "Skypro"`
        """
        if string is None:
            return ""
        return string.capitalize()

    def trim(self, string: str) -> str:
        """
        Принимает на вход текст и удаляет пробелы в начале, если они есть
        Пример: `trim("   skypro") -> "skypro"`
        """
        if string is None:
            return ""
        return string.lstrip()

    def contains(self, string: str, symbol: str) -> bool:
        """
        Возвращает `True`, если строка содержит искомый символ
        и `False` - если нет
        Параметры:
            `string` - строка для обработки
            `symbol` - искомый символ
        Пример 1: `contains("SkyPro", "S") -> True`
        Пример 2: `contains("SkyPro", "U") -> False`
        """
        if string is None or symbol is None:
            return False
        return symbol in string

    def delete_symbol(self, string: str, symbol: str) -> str:
        """
        Удаляет все подстроки из переданной строки
        Параметры:
            `string` - строка для обработки
            `symbol` - искомый символ для удаления
        Пример 1: `delete_symbol("SkyPro", "k") -> "SyPro"`
        Пример 2: `delete_symbol("SkyPro", "Pro") -> "Sky"`
        """
        if string is None:
            return ""
        if symbol is None:
            return string
        return string.replace(symbol, "")
