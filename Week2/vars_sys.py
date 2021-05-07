# If we want to pass in a variable or argument at runtime, we can use the sys library.

import sys

def hello(name):
    print("Hello", name)

name = sys.argv[1]

hello(name)