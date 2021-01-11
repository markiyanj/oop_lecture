from random import randint, choice


class SingletonMetaRealtor(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Realtor(metaclass=SingletonMetaRealtor):
    def __init__(self, name, houses: list, client):
        self.name = name
        self.discount = randint(1, 11)
        self.houses = houses
        self.client = client

    def houses_info(self):
        for house in self.houses:
            print(f'House cost - {house.cost}, house area - {house.area}$ \n')

    # Give a discount for client
    def house_discount(self):
        allow = randint(0, 1)
        if allow == 0:
            discount = self.discount
            print(f'Your discount - {discount}%')
            return discount
        else:
            print('Sorry, I cant`t give you a discount')
            return 0

    def steal_money(self):
        self.client.budget = 0

