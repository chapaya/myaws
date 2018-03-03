import boto3
client = boto3.client('ec2')
response = client.describe_instances()
print(response)
for r in response['Reservations']:
    for instance in r["Instances"]:
        amiid = instance["ImageId"]
        print(amiid) # print all imageid