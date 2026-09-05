
# Python Modules

# -------------------------------------------------
# Program 1: Built-in Module (math)
# -------------------------------------------------

import math

num = 16

print("PROGRAM 1: Built-in Module (math)")
print("Square root:", math.sqrt(num))
print("Factorial:", math.factorial(5))
print("Power:", math.pow(2, 3))
print("Log:", math.log(10))


# -------------------------------------------------
# Program 2: Functional Programming Module
# -------------------------------------------------

from functools import reduce

numbers = [1, 2, 3, 4, 5]

result = reduce(lambda x, y: x + y, numbers)

print("\nPROGRAM 2: Functional Programming Module")
print("Sum using reduce:", result)


# -------------------------------------------------
# Program 3: User-defined Module Concept
# -------------------------------------------------

# User-defined module functions
def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


print("\nPROGRAM 3: User-defined Module Concept")
print("Addition:", add(5, 3))
print("Multiplication:", multiply(4, 2))


# -------------------------------------------------
# Conclusion
# -------------------------------------------------

print("\nConclusion:")
print("Hence, we have successfully used built-in Python modules")
print("and user-defined functions for mathematical and numeric operations.")