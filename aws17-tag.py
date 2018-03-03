import boto3
import sys
# https://gist.github.com/fideloper/a6296b750e8a73d0da1d54b09dd5749e
ec2 = boto3.client('ec2')

# Grab where backup retention is 14 days so we can reduce it to 7
#instances = ec2.describe_instances(Filters=[{'Name': 'tag:Retention', 'Values': ['14']}])
instances = ec2.describe_instances(Filters=[{'Name': 'tag:RI', 'Values': ['yes']}])

ids = []

for reservation in instances['Reservations']:
    for instance in reservation['Instances']:
        print(instance["InstanceId"])
        ids.append(instance['InstanceId'])

print("Changing tags for %d instances" % len(ids))

ec2.create_tags(
    Resources=ids,
    Tags=[
        {
            'Key': 'Retention',
            'Value': '7'
        }
    ]
)

