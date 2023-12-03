# Scenario : We want to fetch the information of our AWS Account Resources and display that.
# And also I don't have access to AWS Console On Production Account as I am consultant and I don't have access, how can we do that ??? 
# This can be achieved with python ( list of ec2, ecr, eks or anything of our choice ) and we want this info to be accessed by the other teammates using NGINX.

# This creates an instance, fetches the list of VM's and displays us.
# ec2 describe instances boto3

import boto3

ec2 = boto3.client('ec2', region_name='us-east-1')       # If you want to handle s3, replace ec2 with s3 in the client

output=ec2.describe_instances()                                 # We are not using any filters
print(output)