# Create two classes: Laptop, Guitar, one for composition, another one for aggregation.
class Devises:
    def __init__(self, mouse, keyboard='bilt-in', microphone='bilt-in'):
        self.mouse = mouse
        self.keyboard = keyboard
        self.microphone = microphone


class OS:
    def __init__(self, os_type, distribution, version):
        self.os_type = os_type
        self.distribution = distribution
        self.version = version


class Laptop:
    def __init__(self, brand, devises: Devises, os: OS):
        self.brand = brand
        self.devises = devises
        self.os = os

    def about_me(self):
        print(f'I`m {self.brand} Laptop witch works on {self.os.os_type} OS')


if __name__ == '__main__':
    devises_list = Devises('Defender Forced GM-020L')
    os = OS('Linux', 'Ubuntu', '20.04.1 LTS')
    dell_laptop = Laptop('Dell', devises_list, os)

    dell_laptop.about_me()
