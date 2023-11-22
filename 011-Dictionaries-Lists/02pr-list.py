import requests 

response = requests.get("https://api.github.com/repos/instana/robot-shop/pulls")
# print(response)                             # status code 
# print(response.json())                    # Prints Entire JSON
# print(type(response.json()))              # Prints the class that's giving JSON

absolute_details = response.json()
exit_code        = response 
response_class   = type(response.json())

print("Printint absolute_details:", absolute_details)
print("Printing exit code :", exit_code)
print("Reponse Class :", response_class)
