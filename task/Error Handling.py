"""
Error Handling in Functions
Write a function that takes a list and an index as arguments. 
The function should try to return the element at the specified index.
If an IndexError occurs, the function should print a friendly error message    
"""
def func(list ,index):
    try:
        return list[index]
    except IndexError:
        print("Error :Index out of range")
        
mylist = [1 ,2 ,3 ,4 ,5] 
print(func(mylist ,2))    

mylist = [6 ,7 ,8 ,9] 
print(func(mylist ,6))       