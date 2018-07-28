import boto3
import datetime
import os
import json
import pprint
import csv

if os.path.exists("somefile.txt"):
    os.remove("somefile.txt")
if os.path.exists("out.csv"):
    os.remove("out.csv")

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
     #print(row['InstanceId'])
     in_id=row['InstanceId']
     print(row['InstanceState']['Name']) # instance status !!
     in_state=row['InstanceState']['Name']
     try:
         value = row['Events']
     except KeyError:
         # Key is not present
         in_name=get_name(fid=row['InstanceId'])
         print("No event for " + row['InstanceId'] + " server_name=" + get_name(fid=row['InstanceId']))
         json_data=row
         x=json.dumps(json_data, sort_keys = True, ensure_ascii=False)
         #pprint.pprint(x)
         #print(row)
         with open('somefile.txt', 'a') as f:
             f.write(x)
             f.write("\n")
         with open('out.csv', 'a') as output:
             writer = csv.writer(output, lineterminator='\n')
             #writer.writerow([in_id])
             line = [in_id,in_name,in_state]
             print(line)
             writer.writerow(line)
     else:
         print("There is event for " + r['InstanceId'] + " server_name=" + get_name(fid=row['InstanceId']) + "Please Check!")

'''
No event for i-0e77545e5a65a2182 server_name=Percona
('{"AvailabilityZone": "us-east-1c", "InstanceId": "i-0e77545e5a65a2182", '
 '"InstanceState": {"Code": 16, "Name": "running"}, "InstanceStatus": '
 '{"Details": [{"Name": "reachability", "Status": "passed"}], "Status": "ok"}, '
 '"SystemStatus": {"Details": [{"Name": "reachability", "Status": "passed"}], '
 '"Status": "ok"}}')


and out.csv with instance id and name and status
'''


