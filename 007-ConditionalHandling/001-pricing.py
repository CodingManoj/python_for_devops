import sys  

color = sys.argv[1]

if color == "blue" :
    print("Blue cars are available") 
elif color == "red" :
    print("Red cars are available") 
elif color == "green" :
    print("Green cars are available") 
else:
    print("Valid Color Options are Blue Green Red Only")