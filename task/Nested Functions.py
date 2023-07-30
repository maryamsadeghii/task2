"""
Nested Functions
Write a function called outer that defines an inner function called inner.
The inner function should print a message, and the outer function should call inner.
Then call outer to see what happens.
"""
def outer():
    def inner():
        print("This is the inner function")
    inner() 
outer()       