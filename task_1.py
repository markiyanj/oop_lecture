# Create a class hierarchy of animals with at least 5 animals that have additional methods each.
from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def eat(self):
        pass


class Cat(Animal):

    def move(self):
        print('I move on 4 legs')

    def eat(self):
        print('Love to hunt mice')

    @staticmethod
    def sleep():
        print('I sleep most of the day')


class Dog(Animal):

    def move(self):
        print('I`m running now!')

    def eat(self):
        print('Love to eat bones')

    @staticmethod
    def protect():
        print('I protect the house')


class Fish(Animal):

    @abstractmethod
    def eat(self):
        pass

    def move(self):
        print('I swim in the water')


class Shark(Fish):

    def eat(self):
        print('I`m hunting on others fish')

    @staticmethod
    def smell():
        print('I can smell the blood at a great distance')


class Bird(Animal):

    def move(self):
        print('I can fly')

    @abstractmethod
    def eat(self):
        pass


class Raven(Bird):

    def eat(self):
        print('I can eat meat and grain')

    @staticmethod
    def study():
        print('I am capable of training')
