"""
Assert Statement
Write a function that takes a list and an index as arguments. Use an assert statement to make sure
the index is within the range of the list. If it's not, raise an AssertionError with a custom error
message. Then call this function with a list and an index to verify it works as expected.    
"""
def func(list ,index):
    assert index < len(list) ,"index out of range"
    return list[index]

my_list = [2 ,3 ,4 ,5 ,6]
num = 8
print(func(my_list , num))
