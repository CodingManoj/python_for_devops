import requests 

url="https://api.github.com/repos/instana/robot-shop/pulls"
response = requests.get(url)
# print(response)                             # status code 
# print(response.json())                    # Prints Entire JSON
# print(type(response.json()))              # Prints the class that's giving JSON

absolute_details = response.json()
exit_code        = response 
response_class   = type(response.json())

# print(absolute_details[0]["user"]["login"])     # This prints only one user., what if I want to know all the users ? Just run a loop
# print("Printing exit code :", exit_code)
# print("Reponse Class :", response_class)
# print(len(absolute_details))                      # Prints the length of the json 

for record in range(len(absolute_details)):
    print(absolute_details[record]["user"]["login"]) 

# Next use case, we also want to display the number of PR's that these users's has made

