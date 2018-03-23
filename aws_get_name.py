import boto3
#https://www.slsmk.com/using-python-and-boto3-to-get-instance-tag-information/
# When given an instance ID as str e.g. 'i-1234567', return the instance 'Name' from the name tag.
ec2 = boto3.resource('ec2')
#fid='i-027a13c48bbd73fa3'
def get_name(fid):
    #ec2instance = ec2.Instance(fid)
    instancename = ''
    print(ec2instance)
    for tags in ec2instance.tags:
        #print(tags) # print all tags
        if tags["Key"] == 'Name':
            instancename = tags["Value"]
            print(instancename)

get_name(fid='i-027a13c48bbd73fa3')