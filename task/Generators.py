"""
Generators
Write a generator function that yields the Fibonacci series. The Fibonacci series is a series of 
numbers in which each number is the sum of the two preceding ones, usually starting with 0 and 1.
Use your generator to print the first 10 numbers in the Fibonacci series.
"""
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

f = fibonacci()
for i in range(10):
    print(next(f))    