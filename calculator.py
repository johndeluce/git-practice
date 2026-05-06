"""This is a simple calculator module that provides basic operations."""


def add(a, b):
    """Return the sum of two numbers"""
    return a + b


def subtract(a, b):
    """Return the difference of two numbers"""
    return a - b


def square(a):
    """Return the square of a number"""
    return a**2


def cube(a):
    """Return the cube of a number"""
    return a**3


if __name__ == "__main__":
    print("Calculator loaded!")
    print(f"5 + 3 = {add(5,3)}")
    print(f"10 - 4 = {subtract(10,4)}")
    print(f"5 squared = {square(5)}")
    print(f"3 cubed = {cube(3)}")


def multiply(a, b):
    """Return the product of two numbers"""
    return a * b


def divide(a, b):
    """Return the quotient of two numbers"""
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b


def power(a, b):
    """Return a raised to the power of b"""
    return a**b


def percentage(value, percent):
    """Calculate percentage of a value"""
    return (value * percent) / 100


print("Calculator ready!")


# Work in progress
def new_feature():
    """A new feature under development"""


# Critical fix
