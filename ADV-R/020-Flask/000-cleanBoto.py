import boto3
from prettytable import PrettyTable

ec2 = boto3.client('ec2', region_name='us-east-1')       # If you want to handle s3, replace ec2 with s3 in the client
instance_list = []
out = ec2.describe_instances()["Reservations"]                     # This gives only one server prop

t = PrettyTable(['InstanceID', 'PrivateIP', 'InstanceType'])
for instances in out: 
    for instance in instances["Instances"]:
        if instance["State"]["Name"] == "terminated":
            continue
        t.add_row([instance["InstanceId"],instance["PrivateIpAddress"],instance["InstanceType"]])   
print(t) 

with open('/usr/share/nginx/html/sample.txt', 'w') as w:
    w.write(str(t))                                             # This writes the file to nginx, where we can access it from the nginx
    
    
# Now we will put this on lambda and see how that works.
