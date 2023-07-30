"""
Try/Except/Finally Block
Write a program that asks the user for a number and prints its square. 
Use a try/except block to handle any errors. No matter what happens, 
print "Execution completed" at the end. Use a finally block for this.    
"""
try:
    number = int(input("Enter a number:"))
    square = number ** 2
    print(f"square of {number} is {square}")
except ValueError:
    print("Error :invalid input.please enter a valid number.")  
finally:
     print("Execution completed")      