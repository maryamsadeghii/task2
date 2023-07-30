"""
Raising Exceptions
Write a function that takes a list and an index as arguments.
If the index is out of range, raise an IndexError with a custom error message.
Call the function with a list and an index, and use a try/except block to handle the error.    
"""
def func(list ,index):
    try:
        if index < 0 or index >= len(list):
           raise IndexError("Index out of range")
    except IndexError:
        print("indexError: ")