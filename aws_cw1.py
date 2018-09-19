from datetime import datetime, timedelta
import boto3

cloudwatch = boto3.client('cloudwatch', region_name='us-east-1')
ec2= boto3.resource('ec2',region_name='us-east-1' )

response = cloudwatch.get_metric_statistics(
    Namespace='AWS/EC2',
    Dimensions=[
        {
            'Name': 'InstanceId',
            'Value': 'i-03165e49a987bebf6'
        },
    ],
    MetricName='CPUUtilization',
    StartTime='2018-07-21T10:10:00',
    EndTime='2018-07-21T18:30:00',
    Period=60,
    Statistics=[
        'Maximum'
    ],
    Unit='Percent',
)

print(response)

counter=0
for cpu in response['Datapoints']:
    print(cpu['Maximum'])
    if float(cpu['Maximum']) > 2:
        print("its over 2%: " + str(cpu['Maximum']))
        counter=counter+1
        print ("The counter is: " + str(counter))
        if counter >3:
            print("counter is over 3 !" + str(counter))


#ec2.create_instances(ImageId='ami-b70554c8',InstanceType='t2.micro', MinCount=1, MaxCount=1)


elb = boto3.client('elb')
lbs = elb.describe_load_balancers()
print(lbs)

response = elb.register_instances_with_load_balancer(
    Instances=[
        {
            'InstanceId': 'i-03165e49a987bebf6',
        },
    ],
    LoadBalancerName='myswslb',
)

print(response)