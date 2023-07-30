"""
**Variable-Length Keyword Arguments (kwargs)
Write a function named print_key_values that takes any number of keyword arguments 
and prints each key-value pair. Call this function with different sets of keyword arguments    
"""
def print_key_value(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} : {value}")
        
print_key_value(name = "maryam" ,age = 22 ,city = "shahryar")     
print_key_value(color = "blue" ,sport = "football")   