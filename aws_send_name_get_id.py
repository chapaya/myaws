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

''' 
output:
 C:\Users\eran\PycharmProjects\aws1\venv\Scripts\python.exe C:/Users/eran/PycharmProjects/myaws/aws_send_name_get_id.py
{'Reservations': [{'Groups': [], 'Instances': [{'AmiLaunchIndex': 0, 'ImageId': 'ami-66506c1c', 'InstanceId': 'i-027a13c48bbd73fa3', 'InstanceType': 't2.medium', 'KeyName': 'opsschool-eran', 'LaunchTime': datetime.datetime(2018, 3, 4, 19, 58, 10, tzinfo=tzutc()), 'Monitoring': {'State': 'disabled'}, 'Placement': {'AvailabilityZone': 'us-east-1a', 'GroupName': '', 'Tenancy': 'default'}, 'PrivateDnsName': 'ip-172-31-12-232.ec2.internal', 'PrivateIpAddress': '172.31.12.232', 'ProductCodes': [], 'PublicDnsName': 'ec2-34-205-87-255.compute-1.amazonaws.com', 'PublicIpAddress': '34.205.87.255', 'State': {'Code': 16, 'Name': 'running'}, 'StateTransitionReason': '', 'SubnetId': 'subnet-311a5455', 'VpcId': 'vpc-44c3e23c', 'Architecture': 'x86_64', 'BlockDeviceMappings': [{'DeviceName': '/dev/sda1', 'Ebs': {'AttachTime': datetime.datetime(2018, 2, 26, 20, 33, 28, tzinfo=tzutc()), 'DeleteOnTermination': True, 'Status': 'attached', 'VolumeId': 'vol-078856ed07259a86d'}}], 'ClientToken': '', 'EbsOptimized': False, 'EnaSupport': True, 'Hypervisor': 'xen', 'NetworkInterfaces': [{'Association': {'IpOwnerId': 'amazon', 'PublicDnsName': 'ec2-34-205-87-255.compute-1.amazonaws.com', 'PublicIp': '34.205.87.255'}, 'Attachment': {'AttachTime': datetime.datetime(2018, 2, 26, 20, 33, 27, tzinfo=tzutc()), 'AttachmentId': 'eni-attach-7449dcb0', 'DeleteOnTermination': True, 'DeviceIndex': 0, 'Status': 'attached'}, 'Description': 'Primary network interface', 'Groups': [{'GroupName': 'default', 'GroupId': 'sg-867dbef2'}], 'Ipv6Addresses': [], 'MacAddress': '02:36:b1:c2:96:b2', 'NetworkInterfaceId': 'eni-3f8edcbf', 'OwnerId': '767137906823', 'PrivateDnsName': 'ip-172-31-12-232.ec2.internal', 'PrivateIpAddress': '172.31.12.232', 'PrivateIpAddresses': [{'Association': {'IpOwnerId': 'amazon', 'PublicDnsName': 'ec2-34-205-87-255.compute-1.amazonaws.com', 'PublicIp': '34.205.87.255'}, 'Primary': True, 'PrivateDnsName': 'ip-172-31-12-232.ec2.internal', 'PrivateIpAddress': '172.31.12.232'}], 'SourceDestCheck': True, 'Status': 'in-use', 'SubnetId': 'subnet-311a5455', 'VpcId': 'vpc-44c3e23c'}], 'RootDeviceName': '/dev/sda1', 'RootDeviceType': 'ebs', 'SecurityGroups': [{'GroupName': 'default', 'GroupId': 'sg-867dbef2'}], 'SourceDestCheck': True, 'Tags': [{'Key': 'Requestedby', 'Value': 'egrimberg'}, {'Key': 'Name', 'Value': 'chef555'}, {'Key': 'APP', 'Value': 'webappops'}, {'Key': 'TagName', 'Value': 'TagValue1'}, {'Key': 'Expiration', 'Value': '2018-04-04'}, {'Key': 'Team', 'Value': 'ops'}, {'Key': 'Owner', 'Value': 'archive'}], 'VirtualizationType': 'hvm'}], 'OwnerId': '767137906823', 'ReservationId': 'r-0c7ed4e739917ccee'}], 'ResponseMetadata': {'RequestId': 'b51666ea-add1-4745-9ee4-083c5297e5ad', 'HTTPStatusCode': 200, 'HTTPHeaders': {'content-type': 'text/xml;charset=UTF-8', 'transfer-encoding': 'chunked', 'vary': 'Accept-Encoding', 'date': 'Mon, 12 Mar 2018 20:55:46 GMT', 'server': 'AmazonEC2'}, 'RetryAttempts': 0}}
x86_64
['i-027a13c48bbd73fa3']

Process finished with exit code 0
'''