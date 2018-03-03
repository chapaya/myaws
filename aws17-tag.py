import boto3
import sys

ec2 = boto3.client('ec2')

# Grab where backup retention is 14 days so we can reduce it to 7
#instances = ec2.describe_instances(Filters=[{'Name': 'tag:Retention', 'Values': ['14']}])
instances = ec2.describe_instances(Filters=[{'Name': 'tag:RI', 'Values': ['yes']}])
ids = []

for reservation in instances['Reservations']:
    for instance in reservation['Instances']:
        ids.append(instance['InstanceId'])

print "Changing tags for %d instances" % len(ids)

ec2.create_tags(
    Resources=ids,
    Tags=[
        {
            'Key': 'Retention',
            'Value': '7'
        }
    ]
)