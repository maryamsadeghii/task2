"""
Nested Try/Except Blocks
Write a program that prompts the user for a filename, then tries to open that file and print
its contents. Use a try/except block to handle any FileNotFoundError. Inside the except block,
prompt the user for a new filename. Continue this until a valid filename is provided and 
the file's contents are printed.    
"""
filename = input("Enter filename:")
while True:
    try:
        with open(filename) as file:
            print(filename)
    except FileNotFoundError:
        print("file not found")
        filename = input("Enter a new filename:")        