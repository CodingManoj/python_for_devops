# Let's execute shell commands using python
# https://docs.python.org/3/library/os.html#os.system 
# os.system() is a function that can do all of OS Actions that's available in OS Module

# import os 
# command = "uptime" 
# output = os.system(command)
# print("System Update is:", output)


import os 
import sys
command = sys.argv[1] 
print("output of command *****", command, "***** is")
output = os.system(command)

# $ python 008-shell.py uptime
#  00:09:32 up  1:25,  0 users,  load average: 0.30, 0.24, 0.35
# 0
# Here we are getting the output of the previous command as well.
# How can I avoid that ?
 