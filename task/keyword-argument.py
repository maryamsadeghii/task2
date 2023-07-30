"""
Keyword Arguments
Write a function named describe_pet that takes two arguments: a pet type and a pet name.
The function should print a description of the pet. Call this function using positional 
and keyword arguments.
"""
def descibe_pet (pet_type ,pet_name):
    print(f"i have a {pet_type} named {pet_name}")

#positional
descibe_pet("cat" ,"Lusy")  

#keyword
descibe_pet(pet_name="hero" ,pet_type="dog")      