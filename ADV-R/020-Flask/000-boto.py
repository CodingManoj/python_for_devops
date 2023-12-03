import boto3
from prettytable import PrettyTable

ec2 = boto3.client('ec2', region_name='us-east-1')       # If you want to handle s3, replace ec2 with s3 in the client
instance_list = []
# op = ec2.describe_instances()
out = ec2.describe_instances()["Reservations"]                     # This gives only one server prop
# Info is a map, so we need to write a loop  ---> How to get data from a list json in python
# op = ec2.describe_instances()["Reservations"]  
# print(op)

# print(out)
# for instances in out:
#     for instance in instances["Instances"]: 
#         print(instance["InstanceId"],instance["InstanceType"], instance["PrivateIpAddress"])


# for instances in out: 
#     for instance in instances["Instances"]:
#         print("|", instance["InstanceId"], "|",  instance["PrivateIpAddress"], "|", instance["InstanceType"],  "|")
# ref : https://stackoverflow.com/questions/9535954/printing-lists-as-tabular-data
# | i-0191688df111a79de | 172.31.39.172 | t3.micro |
# | i-047b2812fbff0245c | 172.31.32.218 | t3.micro |
# | i-07650e27d53ec33b2 | 172.31.42.225 | t3.micro |


# t = PrettyTable(['InstanceID', 'PrivateIP', 'InstanceType'])
# for instances in out: 
#     for instance in instances["Instances"]:
#         t.add_row([instance["InstanceId"],instance["PrivateIpAddress"],instance["InstanceType"]])   
# print(t) 

# +---------------------+---------------+--------------+
# |      InstanceID     |   PrivateIP   | InstanceType |
# +---------------------+---------------+--------------+
# | i-0191688df111a79de | 172.31.39.172 |   t3.micro   |
# | i-047b2812fbff0245c | 172.31.32.218 |   t3.micro   |
# | i-07650e27d53ec33b2 | 172.31.42.225 |   t3.micro   |
# +---------------------+---------------+--------------+

# Now this information has to be accessed over internet.

# But I want to add header to that ?
# Google ---> Printing list as tabular data + Stackoverflow


# Now let's send this output to a file so that it can be server over browser.
# with open('../sample.txt', 'w') as file:
#     file.write(str(t))    # Mention the type as str, if not file write won't happen
    
# 

# But when accessed from the internet it prints the info text, not in a tabular format.
# http://35.175.214.86:5001/index.html
# +---------------------+---------------+--------------+ | InstanceID | PrivateIP | InstanceType | +---------------------+---------------+--------------+ | i-0191688df111a79de | 172.31.39.172 | t3.micro | | i-047b2812fbff0245c | 172.31.32.218 | t3.micro | | i-07650e27d53ec33b2 | 172.31.42.225 | t3.micro | +---------------------+---------------+--------------+
# Google ---> python flask serve raw text file


# You can either let flask server this file or can also also ask nginx to server this file
# Place the index.html file as sample.txt and from browser IP/sample.txt 
# +---------------------+---------------+--------------+
# |      InstanceID     |   PrivateIP   | InstanceType |
# +---------------------+---------------+--------------+
# | i-0191688df111a79de | 172.31.39.172 |   t3.micro   |
# | i-047b2812fbff0245c | 172.31.32.218 |   t3.micro   |
# | i-07650e27d53ec33b2 | 172.31.42.225 |   t3.micro   |
# +---------------------+---------------+--------------+


# So whenever we schedule this and this generates the sample.txt and can server over nginx.

# Also when you terminate any server, during that time script will fail as it can't find that information and we need to hand this!!!

# When any of the server is in terminated state

#   File "boto.py", line 30, in <module>
#     t.add_row([instance["InstanceId"],instance["PrivateIpAddress"],instance["InstanceType"]])
# KeyError: 'PrivateIpAddress'

# May be if the state is Terminate, then just continue  ( )

t = PrettyTable(['InstanceID', 'PrivateIP', 'InstanceType'])
for instances in out: 
    for instance in instances["Instances"]:
        if instance["State"]["Name"] == "terminated":
            continue
        t.add_row([instance["InstanceId"],instance["PrivateIpAddress"],instance["InstanceType"]])   
print(t) 

with open('/usr/share/nginx/html/sample.txt', 'w') as w:
    w.write(str(t))                                             # This writes the file to nginx, where we can access it from the nginx