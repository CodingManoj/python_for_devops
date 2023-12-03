import boto3

ec2 = boto3.client('ec2', region_name='us-east-1')       # If you want to handle s3, replace ec2 with s3 in the client

op = ec2.describe_instances()["Reservations"]["Instances"]                                # We are not using any filters
print(op)           # This gives the data in json, for easy querying, convert this to a Dictionary
