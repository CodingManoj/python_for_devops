# Sys is a module : Module is nothing by a file of funcitons : 
# os is another module to run os commands\
 # Google --->  Os Module Python ( docs.python.org) : https://docs.python.org/3/library/os.html

# os.environ : https://docs.python.org/3/library/os.html#os.environ   ( All the os functions are available here )
# Explore this document.

import os 
home_dir = os.environ["HOME"]            # functions in package os 
print("Prints Home Direcotry Of the User running the script:", home_dir)