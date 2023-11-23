# Let's execute shell commands using python
# https://docs.python.org/3/library/os.html#os.system 
# os.system is a function that can do all of OS Actions

import os 
command = "uptime" 
output = os.system(command)

print("System Update is:", output)