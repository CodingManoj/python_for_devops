# def sum(a,b):
#     val = a + b 
#     print("***Printing Sum ***of a b :", val)

# sum(10,20)

# # python 01-sample.py


# To supply the values from command line : 
# python 01-sample.py 10 20
import sys
def sum(a,b):
    val = a + b 
    print("***Printing Sum ***of a b :", val)

a = int(sys.argv[1])
b = int(sys.argv[2])

def sum(a,b):
    sum = a + b 
    print("***Printing Sum ***of a b :", sum)

def sub(a,b):
    if a > b: 
        diff = a - b
    else:
        diff = b - a 
    print("***Printing Sum ***of a b :", diff)

sum(a,b)
sub(a,b)