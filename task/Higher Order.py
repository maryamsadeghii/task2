"""
Higher Order Functions
Implement the higher order function map yourself. It should take a function and a list as parameters
and apply the function to every element in the list, returning a new list with the results.    
"""
def my_map (func ,list):
    result =[]
    for item in list:
        result.append(func(item))
    return result

mylist = [2 ,3 ,4]  
square = my_map(lambda x : x**2 ,mylist)  
print(square)    