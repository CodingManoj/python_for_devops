# boto3 is a python module from AWS to interact with AWS and create resources.
# All IAC in the backend uses boto.
# Create / update / delete resources using python
# This is a easiest module to use in python.
# For interarctint with AWS, we can also use request module, but using boto3 we can do it in effective way as it's designed for aws.

# There is aws cli, terraform , CFT that creates resources on AWS. ? These 3 are template languages.
# Then what's the use of python boto to create ?
# If we can do with templating, why to use python for aws using boto ?

# In AWS, boto is specifically desinged to take the advantage of serverless and the only choice for you is to use python / go / java to write Lambda functions.
# These situations cannot be handled using bash or cft or tf.

# Install AWS CLI on your computer or on the codeSpace.
# On CodeSpace, on the search bar , search for "> Dev Container" chose "Add Dev Container Configuration Files"
# Click that and select "Modify your active configuration" and then selct the popUp/button and select AWS CLI DevCOntainers
# Then on the left pane you see .devcontainer/devcontainer.json file
# Now on the middle search bar, > rebuild : Now your machine will be rebuild with all the needed or selected images.
# In our case, we would get aws installed.


# aws configure   ( enter access and secret key)
# Now : pip install boto3 ( on your codeSpace )
import boto3

client = boto3.client('s3')

response = client.create_bucket(
    Bucket='manojp-pybucket-0121',
)

# python sc.py # this creates bycket
# Let's say how to get the ACL of this bucket ? searhc for acl in the documentation

# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/get_bucket_acl.html

response = client.get_bucket_acl(
    Bucket='manojp-pybucket-0121',
    ExpectedBucketOwner='string'                  
)

print(response)                           # gives json, conver to dictionary


# boto3 also supports botocore that's used majorly for exception handling.
# when you use boto3 , exception will be handled by default just like ansible

# boto3 vs aws-cli 
# boto3 plays major-role with serverless in aws.

