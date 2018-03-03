import boto3
ec2 = boto3.client('ec2')
filters = [{
         'Name': 'tag:Name',
         'Values': ['']
            }]
reservations = ec2.describe_instances(Filters=filters)
print(reservations)