import re 
# Import is to import a module and we are importing a regular expression module

inspire = "Python For DevOps"
pattern = "for" 

# search is an inbuilt function that finds for the given pattern 
search = re.search(pattern, inspire) 
if search: 
    print("Pattern Found:", search.group())
else: 
    print("Pattern Not Found - - -")