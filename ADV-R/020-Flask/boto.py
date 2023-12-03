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


t = PrettyTable(['InstanceID', 'PrivateIP', 'InstanceType'])
for instances in out: 
    for instance in instances["Instances"]:
        t.add_row([instance["InstanceId"],instance["PrivateIpAddress"],instance["InstanceType"]])   
print(t) 

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
with open('index.html', 'w') as file:
    file.write(t)