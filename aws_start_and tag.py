import boto3
import sys
# Script start all instances that has tag Purpose=KUKU in IR and tag them with Expiration and RequestedBy
# By Eran Grimberg 
# Script get 2 paramaters expiration_date and requested_by and tag the instances .
# start_kuku_servers.py $expiration_date $requested_by

ec2ir = boto3.client('ec2', region_name='eu-west-1')

Expiration_value = sys.argv[1]
Requestedby_value= sys.argv[2]

#print("got:" +Expiration_value)
#print("got:" +Requestedby_value)

instances = ec2ir.describe_instances(Filters=[{'Name': 'tag:Purpose', 'Values': ['KUKU']}]) # All instances that has tag Purpose=KUKU

ids = []

for reservation in instances['Reservations']:
    for instance in reservation['Instances']:
        print(instance["InstanceId"])
        ids.append(instance['InstanceId'])

print(ids)

#Start instances
ec2ir.start_instances(InstanceIds=ids)
print('Started your instances: ' + str(ids))

ec2ir.create_tags(
    Resources=ids,
    Tags=[
        {
            'Key': 'Expiration',
            'Value': Expiration_value
        },
        {
            'Key': 'Requestedby',
            'Value': Requestedby_value
        }
    ]
)

print('Taged your instance ' + str(ids))

