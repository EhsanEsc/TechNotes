# Special Methods(dunder)
'''
__init__
# context management
__enter__
__exit__
# sequence types
__getitem__
__setitem__
__delitem__
# iterable
__iter__
__next__
'''
# Iterable Class
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
'''
# Other
__len__ # implements len()
__contains__ # implements in
'''
'''
creating representation of an object
__repr__
used mostly by developers
can be used for recreating the object
debugging
__str__
used by str() and print()
for displaying to end user, logging, etc
__format__
printing with format
'''
'''
__add__  __sub__  __mul__ __truediv__ / __floordiv__ // __mod__ __pow__ **
__iadd__ += ...
__neg__ __abs__
__lt__ < __le__ <= __eq__ __ne__ __gt__ __ge__
'''
'''
hashing for -> key in dictionaty OR element of set -> implements __hash__ AND implement __eq__
__bool__
'''
class MyClass:
    def __init__(self, name):
        self.name = name
    def __hash__(self):
        return hash(self.name)
    def __eq__(self, other):
        return isinstance(other, MyClass) and self.name == other.name
'''
__call__ -> to implement p()
__del__ -> called before destruction by GC -> don't use it, use context manager instead
'''