# How to exit in python, sys.exit()

import os 
import sys

print("Name of the script :", sys.argv[0])

try:
    def add(a,b):
        sum = a + b 
        return sum 
        sys.exit(0)
except ValueError: 
    print('Not Integer')     
    sys.exit(1)
