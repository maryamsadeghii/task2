"""
Creating Custom Exceptions
Create a custom exception called OutOfRangeError that inherits from Exception.
Write a function that takes a number as an argument and raises an OutOfRangeError
if the number is outside the range 0-10. Call the function with a number and use 
a try/except block to handle the error.    
"""
class OutOfRange(Exception):
    pass
def func(num):
    if num < 0 or num > 10:
        raise OutOfRange("number is out of range")
    
try:
    num = int(input("Enter a number :"))
    func(num)
    print("number in range")
except OutOfRange as e:
    print(e)    