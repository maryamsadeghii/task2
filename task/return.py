"""
Return Values
Write a function named calculate_area that takes the length and width of a rectangle and
returns its area. Use the returned value in a sentence.
For example: "The area of the rectangle is [area]."
"""
def calculate_area (length ,width):
    area = length * width
    return (f"The erea of the rectangle is {area}")

print(calculate_area(2 ,3))
print(calculate_area(4 ,5))
print(calculate_area(3 ,6))
