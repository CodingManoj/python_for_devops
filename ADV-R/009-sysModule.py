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


## Here if you supply integers or float, you get output, if you supply anything apart from that you'd get this out!!!
# ((( Expected Output )))
#  $ python 009-sysModule.py 10 23
# Name of the script : 009-sysModule.py
# Value of a+b is 33.0
# Different of a & b is 13.0 

# (((Unlikely Event)))

# $ python 009-sysModule.py 10 a
# Name of the script : 009-sysModule.py
# Traceback (most recent call last):
#   File "/workspaces/python_for_devops/RGV/009-sysModule.py", line 24, in <module>
#     b_val= float(sys.argv[2])
# ValueError: could not convert string to float: 'a'


# How to handle this, that's why EXCEPTION HANDLING COMES UP (010 for reference)