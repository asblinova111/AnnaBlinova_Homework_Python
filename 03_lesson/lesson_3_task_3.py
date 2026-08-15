from address import Address
from mailing import Mailing

# Создаём экземпляры адресов
to_address = Address("654321", "Санкт-Петербург",
                     "Невский проспект", "20", "5")
from_address = Address("123456", "Москва", "Ленинская", "10", "55")

# Создаём экземпляр класса Mailing (почтовое отправление)
my_mailing = Mailing(to_address, from_address, 1000, "TRACK123456")

# Выводим информацию в нужном формате
print(f"Отправление {my_mailing.track} из {my_mailing.from_address.index}, "
      f"{my_mailing.from_address.city}, {my_mailing.from_address.street}, "
      f"{my_mailing.from_address.house} - {my_mailing.from_address.apartment}в"
      f"{my_mailing.to_address.index}, {my_mailing.to_address.city}, "
      f"{my_mailing.to_address.street}, {my_mailing.to_address.house} -"
      f"{my_mailing.to_address.apartment}. Стоимость {my_mailing.cost} руб.")
