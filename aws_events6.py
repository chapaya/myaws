import boto3
import datetime
import os

if os.path.exists("somefile.txt"):
    os.remove("somefile.txt")

print(datetime.datetime.now())
ec2resource = boto3.resource('ec2')
ec2client = boto3.client('ec2')
#This get_name get instance id and rerutn name
def get_name(fid):
    ec2instance = ec2resource.Instance(fid)
    instancename = ''
    for tags in ec2instance.tags:
        if tags["Key"] == 'Name':
            instancename = tags["Value"]
    return(instancename)
#get_name(fid='i-027a13c48bbd73fa3')

# Check events :
response = ec2client.describe_instance_status()
for row in response['InstanceStatuses']:
     #print(r['InstanceId'])
     try:
         value = row['Events']
     except KeyError:
         # Key is not present
         print("No event for " + row['InstanceId'] + " server_name=" + get_name(fid=row['InstanceId']))
         print(row)
         with open('somefile.txt', 'a') as f:
             f.write('Hello1\n')
             #f.write(row)
     else:
         print("There is event for " + r['InstanceId'] + " server_name=" + get_name(fid=row['InstanceId']) + "Please Check!")

'''
No event for i-0fcc21bbfaea6a592 server_name=spree2
No event for i-0e77545e5a65a2182 server_name=Percona
'''

with open('somefile.txt', 'a') as f:
    f.write('Hello\n')