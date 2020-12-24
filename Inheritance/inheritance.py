class Person():
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def about_me(self):
        print(f'Hi! My name is {self.first_name} {self.last_name} and I am {self.age} years old.')

    def is_able(self):
        print('I can do everything.')


person = Person('John', 'Bridge', '45')
person.about_me()


class Student(Person):
    def learn(self):
        print('I am learning Python')


student = Student('Silvester', 'Dolm', '22')


student.learn()
student.about_me()

class Student(Person):
    def __init__(self, first_name, last_name, age, graduation_year):
        # Person.__init__(self, first_name, last_name, age)
        super().__init__(first_name, last_name, age)
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.graduation_year = graduation_year

    def welcome(self):
        print(f"Welcome {self.first_name} {self.last_name} to the class of {self.graduation_year}.")


student = Student('Silvester', 'Dolm', '22', "2020")


student.about_me()
student.welcome()

is_instance = isinstance(student, Student)
# is_instance = isinstance(1, str)
print(is_instance)

is_subclass = issubclass(bool, int)
# is_subclass = issubclass(float, int)
# is_subclass = issubclass(Student, Person)
print(is_subclass)

class FirstWorker(Person):
    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)

    def is_able(self):
        print('I am first worker and I am able to do that.')


class SecondWorker(Person):
    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)

    def is_able(self):
        print('I am second worker and I am not able to do that.')


class Workers(FirstWorker, SecondWorker):
    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)
        pass


worker = Workers('Adam', 'Smith', '27')
worker.is_able()

# FirstWorker.is_able(worker)
# SecondWorker.is_able(worker)
# Person.is_able(worker)
