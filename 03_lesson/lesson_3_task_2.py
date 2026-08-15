# Импортируем класс Smartphone
from smartphone import Smartphone

# Объявляем переменную catalog — это будет список
catalog = []

# Наполняем список пятью экземплярами класса Smartphone
catalog.append(Smartphone("Apple", "iPhone 15", "+79123456789"))
catalog.append(Smartphone("Samsung", "Galaxy S23", "+79234567890"))
catalog.append(Smartphone("Xiaomi", "Redmi Note 12", "+79345678901"))
catalog.append(Smartphone("OnePlus", "11R", "+79456789012"))
catalog.append(Smartphone("Google", "Pixel 8", "+79567890123"))

# Цикл, который печатает весь каталог в заданном формате
for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
