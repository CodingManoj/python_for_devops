import os 
# name = input("Pls enter your name :")
# print("Name of the user:", name)

folders = input("Enter Directoy Names followed by spaces :").split()
print("List of folders:", folders)

# for folder in folders:
#     print(folder)

# ls in bash is equivalent to os.listdir() in python , listdir is a function in module. 
for folder in folders:
    files = os.listdir(folder) 
    print("------Available files in the given folder ----- :", files)
# printing files of a directory
    for file in files:
        print("*******: ", file)

# If you give an folder that's not there, it reports an error and that's not the expected behavior.
# Exception Handling Matters a lot. Using try and catch we can do that in a very efficient way!
    