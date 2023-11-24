import os 
import sys

print("Name of the script :", sys.argv[0])

try:
    def add(a,b):
        sum = a + b 
        return sum 
except ValueError: 
    print(" Input Error !!!!! Ensure both the supplied values are either int or float !!!!!!")    

try:
    def sub(a,b):
        if a > b:
            diff = a - b 
            return diff 
        else:
            diff = b - a 
            return diff 
except ValueError: 
    print(" Input Error !!!!! Ensure both the supplied values are either int or float !!!!!!")    


a_val= int(sys.argv[1])
b_val= int(sys.argv[2])

print("Value of a+b is", add(a_val, b_val))
print("Different of a & b is", sub(a_val, b_val))
