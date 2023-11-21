import os 

folders = input("Enter Directoy Names followed by spaces :").split()
print("List of folders:", folders)


for folder in folders:
    try:
        files = os.listdir(folder) 
        print("------Available files in the given folder ----- :", files)
    except: 
        print("***** Ensure the directory name is value *****")

    for file in files:
        print("*******:", file)

# If you give an folder that's not there, it reports an error and that's not the expected behavior.
# Exception Handling Matters a lot. Using try and catch we can do that in a very efficient way!

# ls in bash is equivalent to os.listdir() in python , listdir is a function in module. 