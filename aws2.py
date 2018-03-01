#!/usr/bin/env python
import boto3
region = 'XX-XXXXX-X'
# Enter your instances here: ex. ['X-XXXXXXXX', 'X-XXXXXXXX']
instances = ['i-025a9d571f41dcfd2']

ec2client = boto3.client('ec2')
response = ec2client.describe_instances()
for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
        # This sample print will output entire Dictionary object
        #print(instance)
        # This will print will output the value of the Dictionary key 'InstanceId'
        print(instance[instances])


ec2 = boto3.client('ec2')
ec2.start_instances(InstanceIds=instances)
print('started your instances: ' + str(instances))

#ec2_res = boto3.resource('ec2')
#for instance in ec2_res.instances.all():
#    print(instance.id, instance.state)

