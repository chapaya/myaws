import boto3
ec2 = boto3.client('ec2')


#response = ec2.describe_tags()
#print(response)
#for t in response['Tags']:
#    print(t["ResourceType"] , t["Value"])


filters = [{
    'Name': 'ResourceType',
    'Values': ['instance']
    }]
res = ec2.describe_tags(Filters=filters)
print(res)
for x in res['Tags']:
    print(x["Value"])
