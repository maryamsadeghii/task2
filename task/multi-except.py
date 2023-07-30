"""
Try/Except/Else Block
Write a program that tries to open a file and read its contents. If the file does not exist,
print an error message. If the file exists, print its contents.
Use a try/except/else block for this.    
"""
try:
    file = open("file.text")
except FileNotFoundError:
    print("Eror: file not found.")
else:
    contents = file.read()
    print(contents)
    file.close()
        