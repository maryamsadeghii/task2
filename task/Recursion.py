"""
Recursion
Write a function called factorial that uses recursion to calculate the factorial of a number.
Remember that the factorial of a number is the product of all positive integers less than or
equal to that number. Test your function with different numbers.    
"""
def factorial (n):
    if n == 0 :
        return 1
    else :
        return n * factorial(n-1)

print(factorial(4))    
print(factorial(6))    
print(factorial(3))    
print(factorial(0))    

        