class TestClass():
	pass

DynamicTestClass = type('DynamicTestClass', (), {'bar':True})

dtc = DynamicTestClass()

print(dtc)
print(DynamicTestClass)
is_inst = isinstance(dtc, DynamicTestClass)
print(is_inst)

# class NewDynamicTestClass(DynamicTestClass):
# 	pass

NewDynamicTestClass = type('NewDynamicTestClass', (DynamicTestClass,), {})
print(NewDynamicTestClass)
print(NewDynamicTestClass.bar)

print(hasattr(DynamicTestClass, 'bar'))
my_test_class = DynamicTestClass()
my_test_class.bar


# print(TestClass())



class AttributeInitType(type):
	def __call__(self, *args, **kwargs):
		obj = type.__call__(self, *args)
		for name, value in kwargs.items():
			setattr(obj, name, value)
			return obj

class Man(metaclass=AttributeInitType):
	pass

class Man():
	def __init__(self, height, weigth):
		self.height = height
		self.weigth = weigth


me = Man(height=180, weigth=65)
print(type(me))
print(me.height)