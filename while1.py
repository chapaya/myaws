from time import sleep

import boto3
ec2clor = boto3.client('ec2', region_name='us-east-1')
ec2resor = boto3.resource('ec2', region_name='us-east-1')
elb = boto3.client('elb', region_name='us-east-1')

lbname='lb3'
instances='i-02aa1098e70254776'
res = elb.describe_instance_health(
    LoadBalancerName=lbname,
    Instances=[
        {
            'InstanceId': instances
        },
    ]
)


print(res['InstanceStates'][0]['State'])