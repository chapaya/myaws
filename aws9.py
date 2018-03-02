import boto3

# When passed a tag key, tag value this will return a list of InstanceIds that were found.
# Return all tags for specific instance
ec2client = boto3.client('ec2')
tagkey = 'Name'
tagvalue = 'chef111'

response = ec2client.describe_instances(
Filters=[
        {
        'Name': 'tag:'+tagkey,
        'Values': [tagvalue]
        }
        ]
    )
instancelist = []
for reservation in (response["Reservations"]):
    for instance in reservation["Instances"]:
        instancelist.append(instance["InstanceId"])
        print(instance)