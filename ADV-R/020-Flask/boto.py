import boto3
from tabulate import tabulate

ec2 = boto3.client('ec2', region_name='us-east-1')       # If you want to handle s3, replace ec2 with s3 in the client

# op = ec2.describe_instances()
op = ec2.describe_instances()["Reservations"]                     # This gives only one server prop
# Info is a map, so we need to write a loop  ---> How to get data from a list json in python
# op = ec2.describe_instances()["Reservations"]  
# print(op)

for instance in op:
    for IID in instance["Instances"]:
        # print(IID["InstanceId"])
        print(tabulate([['InstanceID', IID["InstanceId"]]],tablefmt='orgtbl'))


# i-0191688df111a79de
# i-047b2812fbff0245c
# i-07650e27d53ec33b2
    
# Let's print the output in tabular format python3


