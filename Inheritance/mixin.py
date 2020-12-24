class BaseClass():
    def test(self):
        print('Base Class')

class Mixin1():
    def test(self):
        print("Mixin1")

class Mixin2():
    def test(self):
        print("Mixin2")

# class MyClass(BaseClass, Mixin1, Mixin2):
#     pass

class MyClass(Mixin2, Mixin1, BaseClass):
    pass

obj = MyClass()
obj.test()
