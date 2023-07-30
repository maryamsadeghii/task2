"""
Basic Try/Except Block
Write a program that asks the user for two numbers and divides the first number by the second number.
If the second number is zero, print an error message. Use a try/except block to
catch theZeroDivisionError.    
"""
try:
    num1 = float(input("Enter the first number:"))
    num2 = float(input("Enter the second number:"))
    result = num1 / num2
    print(f"result is {result}")
except ZeroDivisionError :
    print("Error: Cannot divide by zero")  
    
      