
import sys 

# x=sys.argv[1]  
x=float(sys.argv[1])        # Added float to support decimals, you can leave it as well

if x == 0:
    print("X val is zero --- entered value is :", x)
elif x > 0:
    print("X is greater than 0 --- entered value is :", x)
else:
    print("X is less than 0 --- entered value is :", x)