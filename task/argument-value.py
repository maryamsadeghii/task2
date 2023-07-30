"""
Default Argument Values
Write a function named power that takes two arguments: a number and 
the power to which to raise the number. Give the second argument a default value of 2. 
Call this function with different sets of numbers.
"""
def power (num1 ,num2 = 2):
    return num1 ** num2 

print(power(2))
print(power(3))
print(power(4 ,3))
print(power(1 ,0))
