"""
Logging Exceptions
Write a function that takes a number, divides 10 by the number, and returns the result. 
If a ZeroDivisionError occurs, log the error message with the logging module and raise the error again.
Then, call the function with the number 0 and use a try/except block to handle the ZeroDivisionError.    
"""
import logging
def divided(num):
    try:
        result = 10 / num
        return result
    except ZeroDivisionError as e:
        raise e
    
try:
    divided(0)    
except ZeroDivisionError:
     print("cannot divide by zero.")   