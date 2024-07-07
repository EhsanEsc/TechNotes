class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def f(self):
        print('F Person')

class Student(Person):
    def __init__(self, name, age):
        Person.__init__(self, name, age)
        # super().__init__(name, age) # same as above code
    # Override
    def f(self):
        super().f() # Delegation
        print('F Student')


print(issubclass(Student, Person))
print(issubclass(Student, Student))
s = Student('Ehsan', 22)
p = Person('Person', 23)
print(isinstance(s, Student))
print(isinstance(s, Person))
print(isinstance(s, type(p)))

p.f()
s.f()

# __slots__ for pre_determined attributes of class for faster access and lower memory
# use instance dictionry for add attributes at run-time