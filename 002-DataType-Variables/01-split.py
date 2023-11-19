ARN = "arn:aws:iam::123456789012:user/johndoe"

# Print useName only using inbuilt function

print(ARN.split("/"))                       # gives the elements in a list 

print(ARN.split("/")[1])                    # Printing 2nd element in the list
