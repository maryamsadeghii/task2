"""
Custom Exception with Attributes
Create a custom exception class called OutOfRangeError that inherits from Exception and 
includes an attribute for the invalid value. Write a function that takes a number as an argument 
and raises an OutOfRangeError with the invalid value if the number is outside the range 0-10. 
Then, call the function with a number and use a try/except block to handle the OutOfRangeError
and print the invalid value.       
"""
class OutOfRangeError(Exception):
    def __init__(self,value):
        self.value = value

def func(num):
    if num < 0 or num> 10:
        raise OutOfRangeError("number out of range")  
    
try:
    func(13)    
except OutOfRangeError as e:
    print("Error:",e.value)       