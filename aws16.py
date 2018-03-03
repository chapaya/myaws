import boto3
client = boto3.client('ec2')
response = client.describe_instances()
print(response)  # take the output and use http://jsonviewer.stack.hu/
for r in response['Reservations']:
    for instance in r["Instances"]:
        sgid = instance["SecurityGroups"][0]["GroupId"]
        print(sgid) # print all instances with Reservations/SecurityGroups/GroupId
        rootdisk = instance["RootDeviceName"]
        print(rootdisk)
        state = instance["State"]["Name"]
        print(state)
        tags = instance["Tags"]
        for i in tags:
            print(i)
        print(instance["InstanceId"])
        print("-----------------------------------------------------")

