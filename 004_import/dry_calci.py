import sys

def add(a,b):
    sum = a+b 
    return sum   

def sub(a,b):
    sub = b-a 
    return sub 

def mul(a,b):
    mul = a*b
    return mul

a = sys.argv[1]
operation = sys.argv[2]
b = sys.argv[3]                  # Ensure you import the module

if operation == "add" : 
    output = add(a,b)
    print(output)  
elif operation == "sub" :
    output = sub(a,b)
    print(output)
else:
    output = mul(a,b)
    print(output)

# print("Value Of a+b", addition(5,10))
# print("Value of b-a",substraction(100,200) )
# print("Value of b*a",multiplication(10,40) )