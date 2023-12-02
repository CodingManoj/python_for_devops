# How to exit in python, sys.exit()

import os 
import sys

print("Name of the script :", sys.argv[0])

try:
    sum = a + b 
    return sum 
except ValueError: 
    print('Not Integer')     
    sys.exit(1)                # Exit code 1 would be coming up
