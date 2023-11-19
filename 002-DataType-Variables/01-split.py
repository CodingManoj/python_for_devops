ARN = "arn:aws:iam::123456789012:user/johndoe"

# Print useName only using inbuilt function

print(ARN.split("/"))                       # gives the elements in a list 

print(ARN.split("/")[1])



ProxyPass "/ajay"  "http://172.100.10.20/ajay"
ProxyPassReverse "/ajay"  "http://172.100.10.20/ajay"

ProxyPass "/prakash"  "http://172.100.10.20/prakash"
ProxyPassReverse "/prakash"  "http://172.100.10.20/prakash"
