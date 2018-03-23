import boto3
ec2resource = boto3.resource('ec2')
ec2client = boto3.client('ec2')
#fid='i-027a13c48bbd73fa3'
#This function get instance id and rerutn name
def get_name(fid):
    ec2instance = ec2resource.Instance(fid)
    instancename = ''
    #print(ec2instance)
    for tags in ec2instance.tags:
        #print(tags) # print all tags
        if tags["Key"] == 'Name':
            instancename = tags["Value"]
            #print(instancename)
    return(instancename)

#get_name(fid='i-027a13c48bbd73fa3')
response = ec2client.describe_instance_status()
#print(response)

# Check events :
for r in response['InstanceStatuses']:
     #print(r['InstanceId'])
     try:
         value = r['Events']
     except KeyError:
         # Key is not present
         #print(r['InstanceId'])
         #get_name(fid=r['InstanceId'])
         print("No event for " + r['InstanceId'] + " server_name=" + get_name(fid=r['InstanceId']))
     else:
         print("There is event for " + r['InstanceId'] + " server_name=" + get_name(fid=r['InstanceId']) + "Please Check!")

'''
No event for i-0fcc21bbfaea6a592 server_name=spree2
No event for i-0e77545e5a65a2182 server_name=Percona
'''