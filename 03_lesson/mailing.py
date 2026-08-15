
class Mailing:
    def __init__(self, to_address, from_address, cost, track):
        self.to_address = to_address   # адрес пол.(объект класса Address)
        self.from_address = from_address  # адрес отп.(объект класса Address)
        self.cost = cost                  # стоим-ть,число (напр, 500)
        self.track = track            # трек-номер,строка (напр,"123456789RU")
