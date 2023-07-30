"""
Try/Except/Else/Finally Block
Write a program that prompts the user for a number and calculates its square root.
Use a try/except block to handle cases where the user doesn't input a valid number.
In the else block, print the result of the calculation. In the finally block,
print "Execution completed"    
"""
import math
try:
    number = float(input("Enter a number:"))
    result = math.sqrt(number)
except ValueError:
    print("Error: Invalid input. Please enter a number.")    
else:
    print(f"The square root of {number} is {result}")    
finally:
    print("Execution completed")    

    