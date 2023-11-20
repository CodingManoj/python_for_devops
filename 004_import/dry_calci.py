import sys

def addition(a,b):
    sum = a+b 
    return sum   

def substraction(a,b):
    sub = b-a 
    return sub 

def multiplication(a,b):
    mul = a*b
    return mul

a = sys.argv[1]
b = sys.argv[2]                  # Ensure you import the module

# print("Value Of a+b", addition(5,10))
# print("Value of b-a",substraction(100,200) )
# print("Value of b*a",multiplication(10,40) )