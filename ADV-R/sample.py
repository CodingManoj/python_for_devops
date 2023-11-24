import sys

print("Name of the script :", sys.argv[0])

try:
    value: int(sys.argv[1]) 
    sum = int(sys.argv[1])  +  int(sys.argv[2]) 
    print(sum)
except:
    print('Input As Not A Integer')