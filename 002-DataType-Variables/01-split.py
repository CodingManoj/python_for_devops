ARN = "arn:aws:iam::123456789012:user/johndoe"
PASSWD = "sshd:x:105:65534::/run/sshd:/usr/sbin/nologin"



# Print useName only using inbuilt function

print(ARN.split("/"))                       # gives the elements in a list 
print(ARN.split("/")[1])                    # Printing 2nd element in the list

# Printing UID
print(PASSWD.split(':')[2])