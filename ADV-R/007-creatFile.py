# Google ---> Create file python3 using os module

import os 

name = os.getenv('HOME')
print(name)

with open("/tmp/py.py", "w") as file: 
    file.write("This is a python file \n")
    file.write("This file is written using python")

with open("/tmp/py.py", "r") as readfile:
    filedata=readfile.read()

print("Printing filedata\n\n", filedata)