"""
*Variable-Length Arguments (args)
Write a function named find_max that takes any number of arguments 
and returns the maximum value. Call this function with different sets of numbers
"""
def find_max (*args):
    maximum = max(args)
    return maximum

print(find_max(1 ,3 ,4 ,7 ,9))
print(find_max(11 ,31 ,44 ,57 ,99))