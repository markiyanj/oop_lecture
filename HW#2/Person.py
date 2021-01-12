from abc import ABC, abstractmethod
from random import randint
from Realtor import Realtor


class House:
    def __init__(self, area, cost):
        self.area = area
        self.cost = cost


class Human(ABC):
    @abstractmethod
    def info_about_myself(self):
        pass

    @abstractmethod
    def make_money(self):
        pass

    @abstractmethod
    def buy_a_house(self, house: House):
        pass


class Person(Human):

    def __init__(self, name: str, age: int, availability_of_money: bool, home: bool, salary: int):
        self.name = name
        self.age = age
        self.money = availability_of_money
        self.home = home
        self.salary = salary
        self.budget = 20000 if availability_of_money else 0

    def info_about_myself(self):
        print(f'Hi, my name is {self.name}, i`m {self.age} y.o, my budget - {self.budget}, home - {self.home}')

    def make_money(self):
        self.budget += self.salary

    def work(self, month: int):
        for i in range(month + 1):
            self.make_money()

    def get_discount(self, house: House, discount_percent):
        amount_discount = house.cost * discount_percent / 100
        return amount_discount

    def buy_a_house(self, house: House, discount_percent):
        house_for_discount = house
        discount_percent = discount_percent
        if self.budget > house.cost:
            discount = self.get_discount(house_for_discount, discount_percent)
            self.home = True
            self.budget -= (house.cost - discount)
            print(f'{self.name} bought a house for the price - {house.cost}. His budget - {self.budget}')


if __name__ == '__main__':
    buck = Person('Buck', 37, True, False, 5000)
    buck.info_about_myself()

    apartment = House(40, 30000)
    houses = [apartment]
    realtor = Realtor('Nick', houses, buck)
    realtor.houses_info()

    discount = realtor.house_discount()

    while not buck.home:
        buck.work(1)
        # buck.get_discount(houses[0], discount)

        chance_to_still_money = randint(1, 10)
        if chance_to_still_money == 1:
            realtor.steal_money()
            print('The realtor stole all the money')
        buck.info_about_myself()
        buck.buy_a_house(houses[0], discount)

