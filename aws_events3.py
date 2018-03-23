import boto3
ec2client = boto3.client('ec2')
ec2resource = boto3.resource('ec2')

def get_instance_name( fid ):
    ec2instance = ec2resource.Instance(fid)
    instancename = ''
    for tags in ec2instance.tags:
    if tags["Key"] == 'Name':
        instancename = tags["Value"]
    print(instancename)
    return(instancename)


response = ec2client.describe_instance_status()
#print(response)

for r in response['InstanceStatuses']:
     #print(r['InstanceId'])
     try:
         value = r['Events']
     except KeyError:
         # Key is not present
         get_instance_name(fid = "r['InstanceId']")
         print("No event for " + r['InstanceId'])
     else:
         print("There is event for " + r['InstanceId'] + "Please Check!")
