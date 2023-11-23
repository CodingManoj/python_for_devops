

# Declaring update conf functions 
def update_conf(filepath, key, value): 
    with open(filepath, 'r') as file:                   # Opening the file to read   # with is a system package and no need of any "pip install with"
       lines = file.readlines()                         # Reading the file and storing in a variable in dictionary format
    with open(filepath, 'w') as file:                   # Opening the file in write only mode
        for line in lines:                              # Running the loop against the lines to find the supplied KeyWord
            if key in line:                             # Replacing the Key Value if the key is present
                file.write(key + "=" + value + "\n")
            else:  
                file.write(line)                        # We are just writing the same entry in case of the absense of key


update_conf("server.conf", "MAX_CONNECTIONS", "1711")