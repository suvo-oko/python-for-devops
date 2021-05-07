# Creating reusable variables and functions.
# When we create variables, we need to make sure they can be reused.

def hello():
    name = "Hakim"  # this is a local variable, only accessible inside the function.
    print("Hello", name)

my_name = "Rodrigo"  # this is a global variable, and it can be called anywhere in the code.

def howdy():
    print("Howdy", my_name)

hello()

howdy()

# We can do it like this too

def goodbye(name):
    print("Goodbye", name)

goodbye("Joe")