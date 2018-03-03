import boto3

ec2 = boto3.client('ec2')
response = ec2.describe_instances()
for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
        # This sample print will output entire Dictionary object
        print(instance)
        # This will print will output the value of the Dictionary key 'InstanceId'
        print(instance["InstanceId"])
