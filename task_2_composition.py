# Create two classes: Laptop, Guitar, one for composition, another one for aggregation.

class GuitarType:
    def __init__(self, guitar_type):
        self.guitar_type = guitar_type

    def intro(self):
        print(f'This is {self.guitar_type} guitar')


class Strings:
    def __init__(self):
        self.strings_count = 6


class Guitar:
    def __init__(self, type_of_guitar):
        self.guitar_type = GuitarType(type_of_guitar)
        self.strings = Strings()


if __name__ == '__main__':
    Gibson = Guitar('Acoustic')
    Gibson.guitar_type.intro()
    print(Gibson.strings.strings_count)
