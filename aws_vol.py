import boto3
ec2 = boto3.resource('ec2', region_name='us-east-1')
volumes = ec2.volumes.all()
vol = 'vol-0dd8de038a3c9f8c3'

print(volumes)
for v in volumes:
    print(v.id) # all volumes
    print(v)

print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
volumes = ec2.volumes.filter(Filters=[{'Name': 'status', 'Values': ['available']}]) # if you want to list only available disks - not connected
for v in volumes:
    #print(v.id) # all volumes
    print("This disk is avalible " + v.id)
