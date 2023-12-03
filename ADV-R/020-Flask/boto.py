import boto3

ec2 = boto3.client('ec2', region_name='us-east-1')       # If you want to handle s3, replace ec2 with s3 in the client

# op = ec2.describe_instances()
op = ec2.describe_instances()["Reservations"]                     # This gives only one server prop
# Info is a map, so we need to write a loop  ---> How to get data from a list json in python
# op = ec2.describe_instances()["Reservations"]  
print(op)

for instance in op:
    for IID in instance["Instances"]:
        print(IID["InstanceId"])

    
