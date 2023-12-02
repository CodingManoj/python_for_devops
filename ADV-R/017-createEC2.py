# Google ---> python boto3 aws 
# for any for the aws resource cretion you need to connect to client here in our case it's ec2 

import boto3
import sys 

ec2 = boto3.client('ec2')       # If you want to handle s3, replace ec2 with s3 in the client
count=int(sys.argv[1])
ec2.run_instances(
    ImageId='ami-0f75a13ad2e340a58',
    InstanceType='t3.micro',
    SecurityGroupIds=['sg-052fd946b7e11841a'],
    MaxCount=count,
    MinCount=count,
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'PyNode'
                },
            ]
        },
    ],
)

# Note, there won't be any state, we use python for infra provision with lamdda, where infra or app is immutable 
# python 017-pythonBoto3 

