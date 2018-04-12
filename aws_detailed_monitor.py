
'''
By Eran Grimberg - egrimberg@gmail.com
'''
import boto3
ec2cl = boto3.client('ec2')
response = ec2cl.describe_instances()
print(response)

for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        print("The instance id=" + instance["InstanceId"] + " Monitoring status is " + instance["Monitoring"]["State"])


'''
The instance id=i-xxxxx Monitoring status is disabled
The instance id=i-xxxxx Monitoring status is disabled
'''
