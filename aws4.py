# http://www.pwebdev.com/aws-instances-using-boto3/

import boto3
ec2 = boto3.resource('ec2')
instances = ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
for instance in instances:
  print("Instance id - ", instance.id)
  print("Instance public IP - ", instance.public_ip_address)
  print("Instance private IP ", instance.private_ip_address)
  print("----------------------------")