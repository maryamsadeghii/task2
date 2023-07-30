"""
Closure
Write a closure function named power_n that raises a number to the power of n.
The outer function should take n as a parameter, and the inner function should take the number as a parameter. 
Use your closure with several different powers and numbers.
"""
def power_n (n):
    def inner (num):
        return num ** n
    return inner

power = power_n(2)
print(power(3))

power = power_n(3)
print(power(2))
    