
# Напишите функцию month_to_season(), которая принимает один аргумент
# номер месяца — и возвращает название сезона,к которому
# относится этот месяц. Например, передаем 2,
# на выходе получаем «Зима».


def month_to_season(num_month):
    if num_month in [12, 1, 2]:
        return "Зима"
    elif 3 <= num_month <= 5:
        return "Весна"
    elif 6 <= num_month <= 8:
        return "Лето"
    elif 9 <= num_month <= 11:
        return "Осень"
    else:
        return "Неверный номер месяца"


num_month = int(input("Введите номер месяца (1-12): "))
print(month_to_season(num_month))
