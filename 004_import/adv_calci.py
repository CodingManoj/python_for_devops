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

def multiplication(a,b):
    mul = a*b
    return mul

print("Value Of a+b", addition(5,10))
print("Value of b-a",substraction(100,200) )
print("Value of b*a",multiplication(10,40) )


'''Even this is not a good way to using variables as everytime ,we nee to come and update file. Use Environment Variables or Arguments as mentioned in 005'''
# Using the modules appraoch we can make use of it. Use dry_calci.py