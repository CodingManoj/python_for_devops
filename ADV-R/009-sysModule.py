# Google ---> sys module python for all the other options
# argv[0]  is going to print the script name


import os 
import sys

print("Name of the script :", sys.argv[0])

def add(a,b):
    sum = a + b 
    return sum 

def sub(a,b):
    if a > b:
        diff = a - b 
        return diff 
    else:
        diff = b - a 
        return diff 


a_val= float(sys.argv[1])
b_val= float(sys.argv[2])

print("Value of a+b is", add(a_val, b_val))
print("Different of a & b is", sub(a_val, b_val))
