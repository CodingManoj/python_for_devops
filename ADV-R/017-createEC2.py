import boto3

ec2 = boto3.client('ec2')       # If you want to handle s3, replace ec2 with s3 in the client

ec2.run_instances(
    ImageId='ami-0f75a13ad2e340a58',
    InstanceType='t3.micro',
    SecurityGroupIds=['sg-052fd946b7e11841a'],
    TagSpecifications=[
        {
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'PyNode'
                },
            ]
        },
    ],
)

