import boto3

# Region your instances are in, e.g. 'us-east-1'
#region = 'XX-XXXXX-X'

# instances ID: ex. ['X-XXXXXXXX', 'X-XXXXXXXX']
instances = ['i-025a9d571f41dcfd2']   #chef111
#ec2 = boto3.client('ec2', region_name=region)
ec2 = boto3.client('ec2')
ec2.stop_instances(InstanceIds=instances)
print 'stopped your instances: ' + str(instances)
