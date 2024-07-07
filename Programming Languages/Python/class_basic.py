class Person:
  # Class Attributes
  version = '1.22'
  # Initialize class
  def __init__(self, name, age):
    # Instance Attributes
    self.name = name
    self.age = age
  # Method
  def myfunc(self):
    print("Hello my name is " + self.name)

print(getattr(Person, 'version'))
setattr(Person, 'version', '1.23')
print(Person.version)
delattr(Person, 'version')
print(Person.__dict__)

p1 = Person("John", 36)
print(type(p1))
print(isinstance(p1, Person))
p1.myfunc()
Person.myfunc(p1)
p1.asdf = 22
del p1.asdf
del p1


# Property
class MyClass:
  def __init__(self, name, family):
    self._name = name
    self._family = family
  
  def get_name(self):
    return self._name
  
  def set_name(self, name):
    if len(name) > 0:
      self._name = name
    else:
      raise ValueError('Name must not be empty!')

  name = property(fget=get_name, fset=set_name)

  @property
  def family(self):
    return self._family
  @family.setter
  def family(self, value):
    self._family = value

mc = MyClass('Ehsan', 'Esc')
print(mc.name)
print(mc.get_name())
mc.name = 'Ali'
print(mc.get_name())
try:
  mc.name = ''
except ValueError as e:
  print(e)

# Static and class methods
class AnotherClass:
  def instance_f(self):
    print(f'hi instance {self}')
  
  # Can access to attributes of class
  @classmethod
  def class_f(arg):
    print(f'hi class {arg}')
  
  @staticmethod
  def static_f():
    print('hi static')

print('@@@')
ac = AnotherClass()
ac.instance_f()
ac.class_f()
ac.static_f()
# AnotherClass.instance_f() -> Error
AnotherClass.class_f()
AnotherClass.static_f()