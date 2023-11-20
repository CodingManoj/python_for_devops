''''

Multie Line Comment In Python 

a  = 100
b  = 200 

def addition():
    sum = a+b 
    print("Value of a + b is :", sum)

def substraction():
    sub = b-a 
    print("Value of b-a is :", sub)

def multiplication():
    mul = b * a 
    print("Value of b*a is :", mul)

addition()
substraction()
multiplication()

This is not a great way as this don't have much modularity. The same can be done in a better way using this approach

'''

'''Always Keep In Mind : Function Should Take the Input : Perform the Task : Return the Output'''

def addition(a,b):
    sum = a+b 
    return sum   

def substraction(a,b):
    sub = b-a 
    return sub 

print("Value Of a+b", addition(5,10))
print("Value of b-a",substraction(100,200) )