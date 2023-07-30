"""
Multiple Except Blocks
Modify the previous program to also handle a situation where the user inputs something 
that's not a number. Use a separate except block to catch a ValueError.    
"""
try:
    num1 = float(input("Enter the first number:"))
    num2 = float(input("Enter the second number:"))
    result = num1 / num2
    print(f"result is {result}")
except ZeroDivisionError :
    print("Error: Cannot divide by zero") 
except ValueError:
    print("Error: Invalid input. Please enter a number.")    