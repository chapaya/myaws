import boto3

# When given an instance ID as str e.g. 'i-1234567', return the instance 'Name' from the name tag.
ec2 = boto3.resource('ec2')
#instances = ['i-025a9d571f41dcfd2']   #chef111
ec2instance = ec2.Instance('i-025a9d571f41dcfd2')
instancename = ''
for tags in ec2instance.tags:
    if tags["Key"] == 'Name':
        instancename = tags["Value"]
        print(instancename)