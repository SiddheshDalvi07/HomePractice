import modulee
from modulee import *
print(add(2, 3)) # Output: 5
print(subtract(7, 4)) # Output: 3 

print(dir())  # List of all the functions and variables in current module
print(dir(modulee))  # List of all the functions and variables in 'modulee.py'</s>
print(person.items())

print(x)

print(__name__)


def fib(n):    # write fibonacci series up to n



    a, b = 0, 1

    while a < n:

        print(a, end=' ')

        a, b = b, a+b

    print()

fib(20)

