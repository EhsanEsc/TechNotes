
#https://www.w3schools.com/python/python_reference.asp


###################
# Introduction to Python
# A brief guide to Python basic syntaxes
# ------------------------------------- Variables -------------------------------------------

name = "Mike"    # Strings
age = 30         # Integer
gpa = 3.5         # Decimal (Floats)
is_tall = True    # Boolean -> True/False (First Letter is capital)
name = "John"
# Printing in Two Ways
print("Your name is " + name)
print("Your name is", name)
print("bitcoin is %i dollars" % 12)
# --------------------------------- Casting and Converting ----------------------------------

print(type(gpa))
print(int(3.14))
print(float(3))
print(int("50") + int("70"))  # Converting String to Number (Wow!!)
# ---------------------------------------- Strings ------------------------------------------

greeting = "Hello"
# indexes:   01234
# indexes:   -5,-4,-4,-2,-1

print(len(greeting))  # Length of the String
print(greeting[0])
print(greeting[-1])  # Second Form of Indexes

# Finding a Substring
print(greeting.find("llo"))  # Result = 2
print(greeting.find("z"))  # Result = -1 (Not Found)
print(greeting[2:])  # from index 2 to end
print(greeting[2:3]) # (]
print(greeting, age)
print(greeting*2)  # HelloHello

str1 = "Ehsan "
str2 = "  Escandari    "
str = f'{str1} and {str2}'

print(str1 + str2)
print(str2.strip())
print(str1.lower())
print(str2.upper())
print(str2.replace("a", "z"))
str2 = str2.replace(" ", "")
str3 = "Ehsan,Escandari"
print(str3.split(","))

# ---------------------------------------- Numbers ---------------------------------------------

print(2 * 3)       # Basic Arithmetic: +, -, /, *  Result = 6
print(2**3)        # Basic Arithmetic: +, -, /, *  Result = 8
print(10 % 3)      # Modulus Op. : returns remainder of 10/3  Result = 1
print(1 + 2 * 3)   # order of operations  Result = 9
print(10 / 3.0)      # int's and doubles  Result = 3.333333333
print(10 / 3)        # Result = 3.33333333 (WHAT??!!)(You Should Keep This in Mind)
print(10 // 3)       # Result = 3 (Compare with upper line!)
num = 10
num += 100  # +=, -=, /=, *=
print(num)
# ------------------------------------ Getting Inputs -------------------------------------------

# name = input("Enter your name: ")  # Inputs are saved as Strings by Default
# print("Hello", name + "!")
# num1 = int(input("Enter First Num: "))  # String to int
# num2 = int(input("Enter Second Num: "))
# print(num1 + num2)
# ----------------------------- Lists (Very Similar to Arrays & Vectors) -------------------------

# We can have any kind of types in a list in the same time
lucky_numbers = [4, 8, "fifteen", 16, 23, 42.0]
#       indexes  0  1       2      3   4   5

# access
lucky_numbers[0] = 90
print(lucky_numbers[0])  # Result : 90
print(lucky_numbers[1])  # Result : 8
print(lucky_numbers[-1])  # Result : 42.0
print(lucky_numbers[2:])  # Result : ['fifteen',16,23,42.0]
print(lucky_numbers[2:4])  # Result : ['fifteen',16]
print(len(lucky_numbers))  # Result : 6
x = range(10)  # x = [0,1,.....,9]
# ----------------------------------- N Dimensional Lists -----------------------------------------

numberGrid = [[1, 2], [3, 4]]
numberGrid[0][1] = 99

print(numberGrid[0][0])  # 1
print(numberGrid[0][1])  # 99
# ------------------------------------- List Functions ---------------------------------------------

friends = []
friends.append("Oscar")  # append == push_back in Vectors
friends.append("Angela")
friends.append("Oscar2")
friends.append("Oscar3")
friends.append("Oscar4")
# push back in index 1 (it shifts every values that are after it one time)
friends.insert(1, "Kevin")
print(friends)  # It Prints the whole List(Wow!!)

# Access
print(friends.index("Oscar"))  # It returns the index of the element "Oscar"
print(friends.count("Angela"))  # It returns the Count of repeat times

# Sorting
friends.sort()  # Sorting by Alphabet -> Angela , Kevin , Oscar
print(friends)
friends.reverse()
friends.sort(reverse=True)

def myfunc(n):
  return abs(n - 50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)


# pop : delete by index(or last index)
# remove : delete by value if it is not in list has runtime error
# del : delete by index
friends.remove("Kevin")  # Removes Kevin from list
print('###', friends)
friends.pop()
friends.pop(1)
print('###', friends)
del friends[1]
friends.clear()  # clears the whole list
print(friends)
1 in [1, 2, 3]  # True
0 in [1, 2, 3]  # False
y = [1, 2, 3]
# any iterable object can be used for extend function
y.extend([4, 5, 6])  # y = [1,2,..,6] 
# Unpacking
a, b = [1, 2]  # now a is 1 & b is 2 (Unpacking lists)
_, y22 = [1, 2]  # now y is 2 & we don't care what the first element is
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits

[print(x) for x in y]
for x in y:
    print(x)
newlist = [x for x in y if x==1]
newlist = [x*x for x in range(10)] 
#  newlist = [expression for item in iterable if condition == True] 

# Copy
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
mylist = list(thislist)

# ----------------------------------------- Tuples ----------------------------------------------

# It is just like Arrays but its Immutable(Can not be Changed)
lucky_numbers = (4, 8, "fifteen", 16, 23, 42.0)

# Merging two tuple or add to tuple
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
#
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

# Functions
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.count(5)
x = thistuple.index(8)
# ---------------------------------------- Sets --------------------------------------------------

# A set is a collection which is unordered and unindexed.
new_set = {"apple", "banana", "cherry", 2}
print(new_set)
# Sets are unordered, so you cannot be sure in which order the items will appear.

# You cannot access items in a set by referring to an index
for itr in new_set:
    print(itr)

# set items are immutable(Can not be Changed) but we can add items to it
# adding 1 item --> add()
# adding multiple items --> update()
new_set.add(3)
new_set.update(["orange", "mango", "grapes"])
print(new_set)
print(len(new_set))
new_set.remove("orange")  # remove orange from set
new_set.discard("orange") # Remove(not raised error if not found)
new_set.pop()  # remove last item(Random Item)
new_set.clear()  # remove all items
del new_set  # remove the set

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
# Join
set3 = set1.union(set2)
set1.update(set2)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y) # x.symmetric_update(y)
z = x.intersection(y)
x.intersection_update(y)
# ---------------------------------------- Functions ----------------------------------------------

# We should use def to define a function


def add_numbers(num1, num2=99):  # look at The ":"  and  Indentation
    return num1 + num2


sum = add_numbers(4, 3)
print(sum)  # 7
sum = add_numbers(4)
print(sum)  # 103
sum = add_numbers(num1=4)
print(sum)  # 103 (Just like the previous one)

def my_function(*kids): # Arbitrary Arguments 
  print("The youngest child is " + kids[-1])
my_function("Emil", "Tobias", "Linus")

def my_function2(**kid):
  print("His last name is " + kid["lname"])
my_function2(fname = "Tobias", lname = "Refsnes") 
def myfunction3():
  pass
# We can Pass Functions to others just like variables
def multiplyByTwo(add_numbers, num):
    return(add_numbers(num, num))

def list_comp_square(n):
    return [i**2 for i in range(0, n) if i % 2 == 0]

def myfunc():
  global x
  x = 300
myfunc()
print(x) 

# ---------------------------------------- Lambda ----------------------------------------------
# lambda arguments : expression 
x = lambda a : a + 10
print(x(5)) 
x = lambda a, b : a * b
print(x(5, 6)) 

def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
print(mydoubler(11))
# ---------------------------------------- If Statements -------------------------------------------

is_student = False
is_smart = False

# Be careful about ":" and indentation
# && --> and
# || --> or
# !  --> not
if is_student and is_smart:
    print("You are a student")
elif is_student and not(is_smart):  # else if --> elif
    print("You are not a smart student")
else:
    print("You are not a student and not smart")

# You Can use below operators too !!
# >, <, >=, <=, !=, ==
if 1 > 3:
    print("number omparison was true")

if "dog" == "cat":
    print("string omparison was true")
# ------------------------------------------ Dictionaries -------------------------------------------

# It is like a Map (Keys and Values) (Keys should be unique)
test_grades = {
    "Andy": "B+",
    "Stanley": "C",
    "Ryan": "A",
    3: 95.2
}
print(test_grades["Andy"])  # B+
# if the key couldnt be found "No Student Found" will be printed instead
print(test_grades.get("Ryan", "No Student Found"))
print(test_grades[3])  # 3 is not the index but the key "3"
# View of dictionary
z = test_grades.keys()
z = test_grades.values()
# return each item in a dictionary, as tuples in a list.
z = test_grades.items() 
test_grades.update({"Mamad": "A"})
x = test_grades.pop("Mamad")
test_grades.popitem()
for x, y in test_grades.items():
  print(x, y)
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  }
} 
x = ('key1', 'key2', 'key3')
y = 0
thisdict = dict.fromkeys(x, y)
# ------------------------------------------ While Loops --------------------------------------------

index = 1
# Be careful about ":" and indentation
while index <= 5:
    print(index)
    index += 1
# ------------------------------------------ For Loops ----------------------------------------------

# i will automatically start at 0
for i in range(5):  # range(0,5) : (>=0 and <5)
    print(i)

# Looping through a whole list
lucky_nums = [4, 8, 15, 'cat', 23, 42]
for lucky_num in lucky_nums:
    print(lucky_num)

# Looping through words of a string
for letter in "Giraffe":
    print(letter)
# break, continue
# ------------------------------------- Exception Handling -------------------------------------------

try:
    # answer = 10 / int(input("Enter Number: "))
    answer = 10 / 0

# ZeroDivisionError & ValueError are two default classes in Python

except ZeroDivisionError as e:  # Storing this kind of error in variable "e"
    print(e)
except ValueError as e:
    print(e)
except:  # general (Not Recommended !!)
    print("Caught any exception")
# ------------ Iterators ----- #
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

# ------------ Formatting ---- #

age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))

# ------------ OTHER --------- #

str = ["a","b","c"]
for letter in enumerate(str):
    print(letter[0])
for ind,let in enumerate(str):
    print(ind,let)

#comment
""" another
commnet """

# Import
"""
# aaa.py
def greeting(name):
  print("Hello, " + name) 
x = 22
# b.py
import aaa as a 
a.greeting("Jonathan")
y = a.x
print(dir(a))

from aaa import x
print(x)

"""

# --------------------------- #
# Strong and Weak Refrence
import weakref
class MyClass:
  pass
p1 = MyClass()
p2 = p1 # both strong, refrence count for garbage collector
p3 = weakref.ref(p1) # p3 is weak refrence. if p1 and p2 deleted, object will be garbade collected

# --------------------------- #
# Enum type
import enum
class Color(enum.Enum):
  RED = 1
  GREEN = 2
  BLUE = 3
print(Color.RED, type(Color.RED), isinstance(Color.RED, Color))
print(Color.RED.name, Color.RED.value)
print(list(Color))
for c in Color:
   print(repr(c))
# we can have unique and alias as well

###


# en = input()
exit()
