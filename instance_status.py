#https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#instance

import boto3

ec2 = boto3.resource('ec2')
instance = ec2.Instance('i-0a5448168783adce5')
print(instance.state)

for instance in ec2.instances.all():
    print(instance.id, instance.state)
    
'''
{'Code': 16, 'Name': 'running'}
i-0a5448168783adce5 {'Code': 16, 'Name': 'running'}
'''
