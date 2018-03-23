import boto3
import datetime
ec2 = boto3.client('ec2')
ec2res = boto3.resource('ec2')
t=datetime.datetime.now() - datetime.timedelta(0)
print(t)
f=datetime.datetime.now() - datetime.timedelta(10)
print(f)

instances = ec2.describe_instances(Filters=[{'Name': 'tag:Owner', 'Values': ['archive']}]) # All instances that has tag owner=archive

ids = []

for reservation in instances['Reservations']:
    for instance in reservation['Instances']:
        print(instance["InstanceId"])

        ids.append(instance['InstanceId'])

print(ids)

status=ec2.get_all_instance_status(instance_ids=i-025a9d571f41dcfd2)
print(status[0].system_status.details)

#print(res)
