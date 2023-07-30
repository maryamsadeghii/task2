"""
Exception Chaining
Write a function that takes a string as an argument, tries to convert the string to an integer,
and returns the integer. If a ValueError is raised, catch it and raise a TypeError from it with
a custom error message. Then, call the function with a string and use a try/except block to
handle the TypeError.    
"""
def func(string):
    try:
        integer = int(string)
        return integer
    except ValueError as e:
        raise TypeError("Invalid input. Please provide a valid integer.") from e

try:
    result = func("b")
except TypeError as e:
    print("Error:", str(e))
