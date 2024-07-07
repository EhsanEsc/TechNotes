### Decorator
# E1
# This simplest decorator does nothing to the function being decorated. Such
# minimal decorators can occasionally be used as a kind of code markers.
def super_secret_function(f):
    return f
@super_secret_function
def my_function():
    print("This is my secret function.")

# E2
def print_args(func):
    def inner_func(*args, **kwargs):
        print(args)
        print(kwargs)
        return func(*args, **kwargs) #Call the original function with its arguments.
    return inner_func
@print_args
def multiply(num_a, num_b):
    return num_a * num_b
print(multiply(3, 5))
#Output:
# (3,5) - This is actually the 'args' that the function receives.
# {} - This is the 'kwargs', empty because we didn't specify keyword arguments.
# 15 - The result of the function.

# E3
class Decorator(object):
    """Simple decorator class."""
    def __init__(self, func):
        self.func = func
    def __call__(self, *args, **kwargs):
        print('Before the function call.')
        res = self.func(*args, **kwargs)
        print('After the function call.')
        return res
@Decorator
def testfunc():
    print('Inside the function.')
testfunc()
# Before the function call.
# Inside the function.
# After the function call.

### With Statement
# Safely open the file
file = open("hello.txt", "w")

try:
    file.write("Hello, World!")
except Exception as e:
    print(f"An error occurred while writing to the file: {e}")
finally:
    # Make sure to close the file after using it
    file.close()
# Context management protocol 
# with expression as target_var:
#     do_something(target_var)

    # .__enter__() is called by the with statement to enter the runtime context.
    # .__exit__() is called when the execution leaves the with code block.

with open("hello.txt", mode="w") as file:
    file.write("Hello, World!")

# Custom context management protocol
class HelloContextManager:
    def __enter__(self):
        print("Entering the context...")
        return "Hello, World!"
    def __exit__(self, exc_type, exc_value, exc_tb):
        print("Leaving the context...")
        print(exc_type, exc_value, exc_tb, sep="\n")


with HelloContextManager() as hello:
    print(hello)
# ...
# Entering the context...
# Hello, World!
# Leaving the context...
# None
# None
# None
