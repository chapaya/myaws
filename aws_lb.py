
import boto3

elb = boto3.client('elb' ,region_name='us-east-1')
lbs = elb.describe_load_balancers()
print(lbs)

print(lbs['LoadBalancerDescriptions'])


for lb in lbs['LoadBalancerDescriptions']:
    print(lb['LoadBalancerName'])

print(elb.waiter_names)

