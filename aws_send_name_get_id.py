import boto3
#https://www.slsmk.com/using-python-and-boto3-to-get-instance-tag-information/
# When passed a tag key, tag value this will return a list of InstanceIds that were found.

ec2client = boto3.client('ec2')
tagkey='Name'
tagvalue='chef555'
response = ec2client.describe_instances(
    Filters=[
        {
            'Name': 'tag:'+tagkey,
            'Values': [tagvalue]
        }
    ]
    )
print(response) # Take this output and put in http://jsonviewer.stack.hu/
instancelist = []
for reservation in (response["Reservations"]):
    for instance in reservation["Instances"]:
        print(instance["Architecture"])
        instancelist.append(instance["InstanceId"])
print(instancelist)