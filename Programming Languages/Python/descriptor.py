'''
descriptor protocol
__get__
__set__
__delete__
__set_name__
2 types
__get__ only -> non-data descriptor
with set and delete -> data descriptor
'''
from datetime import datetime
class TimeUTC:
    def __get__(self, instance, owner_class): # instance will be None, if it called directly from Class
        if instance is None:
            return self
        return datetime.utcnow().isoformat()
class Logger:
    current_time = TimeUTC() # Class Attribtue
l = Logger()
print(l.current_time)
print(Logger.current_time)

# Storing data in descriptor class instead of instance
class IntegerValue:
    def __init__(self):
        self.data = {}
        # with weakref to avoid memory leak
        # self.data = weakref.WeakKeyDictionary()

    def __set__(self, instance, value):
        self.data[instance] = int(value)
    def __get__(self, instance, owner_class):
        if not instance:
            return self
        return self.data.get(instance)

class Point2D:
    x = IntegerValue()
    y = IntegerValue()
p1 = Point2D()
p2 = Point2D()
p1.x = 1.1
p1.y = 10.2
p2.x = 2.1
p2.y = 20.2
print(p1.x, p1.y)
print(p2.x, p2.y)
print(Point2D.x.data)

# Can use __set_name__ for better logging and
# Storing data in instance
class StringValue:
    def __init__(self):
        pass

    def __set_name__(self, owner_class, property_name):
        self.property_name = property_name
    def __set__(self, instance, value):
        instance.__dict__[self.property_name] = value
    def __get__(self, instance, owner_class):
        if not instance:
            return self
        return instance.__dict__.get(self.property_name)
class Person:
    first_name = StringValue()
    last_name = StringValue()
p1 = Person()
p2 = Person()
p1.first_name = 'Ehsan'
p1.last_name = 'Esc'
p2.first_name = 'MH'
p2.last_name = 'Ro'
print(p1.first_name, p1.last_name)
print(p2.first_name, p2.last_name)