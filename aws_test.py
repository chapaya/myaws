import boto3

ec2 = boto3.client('ec2')

instances = ec2.describe_instances(Filters=[{'Name': 'tag:Owner', 'Values': ['archive']}]) # All instances that has tag owner=archive

ids = []

for reservation in instances['Reservations']:
    for instance in reservation['Instances']:
        print(instance["InstanceId"])
        ids.append(instance['InstanceId'])

print(ids)

#Start instances
ec2.start_instances(InstanceIds=ids)
print('Started your instances: ' + str(ids))

ec2.create_tags(
    Resources=ids,
    Tags=[
        {
            'Key': 'Expiration',
            'Value': '2018-04-04'
        }
    ]
)
ec2.create_tags(
    Resources=ids,
    Tags=[
        {
            'Key': 'Requestedby',
            'Value': 'egrimberg'
        }
    ]
)
print('Taged your instance ' + str(ids))