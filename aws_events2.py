import boto3

client = boto3.client('ec2')

response = client.describe_instance_status()
#print(response)

for r in response['InstanceStatuses']:
     #print(r['InstanceId'])
     try:
         value = r['Events']
     except KeyError:
         # Key is not present
         print("No event for " + r['InstanceId'])
     else:
         print("There is event for " + r['InstanceId'] + "Please Check!")


