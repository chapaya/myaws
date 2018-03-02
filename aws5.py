import boto3
ec2 = boto3.resource('ec2')
instances = ec2.instances.filter(
    Filters=[{'Name': 'instance-state-name', 'Values': ['running','stopped']}]
    )
for instance in instances:
    print(instance.id ,instance.state)