names = ["mike","steve","john"]
# names = ("mike","steve","john")
print("Printing length:", len(names))
names.append("christman")              # This append will only work for list, not for append.
print(names)
print("Printing type:", type(names))
print("Printing length:", len(names))

# Removes an element from the list 

names.remove("steve")
print("Printing length:", len(names))
print("Printing list:", names)


numbers = [10,15,30,11,12]
numbers.sort()
print(numbers)

#Lists can also contains elements of various datatypes
mychoice = ["manoj" ,10, "devops"]
print(mychoice)