
# Declaring Global Variables 
a = 100 
b = 50 

# delcarting functions
def addition():
    print("Sum: ", a+b) 

def sub():
    a = 150                  # Declaring local funcion
    print("sub:" ,a-b) 

# Calling functions
addition()
sub()