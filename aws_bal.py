'''
This Script checks instance status of instances in LB <Eran Grimberg 20180724>
'''
from time import sleep

import boto3
ec2clor = boto3.client('ec2', region_name='us-east-1')
ec2resor = boto3.resource('ec2', region_name='us-east-1')
elb = boto3.client('elb', region_name='us-east-1')

def get_name(fid):
    ec2instance = ec2resor.Instance(fid)
    instancename = ''
    for tags in ec2instance.tags:
        if tags["Key"] == 'Name':
            instancename = tags["Value"]
    return(instancename)

def check_status(fid):
    res = elb.describe_instance_health(
        LoadBalancerName=lbname
    )
    for ec2list in res['InstanceStates']:
        if ec2list['InstanceId']==fid:
            print(ec2list['State'])
    return(ec2list['State'])


lbname='lb3'

res = elb.describe_instance_health(
    LoadBalancerName=lbname
    )

counter=0
print("Here is the instances status for load balancer: " + lbname)
for ec2list in res['InstanceStates']:
    print("InstanceId: " + ec2list['InstanceId'] + " - " + get_name(fid=ec2list['InstanceId']) + " - " + ec2list['State'])
    if ec2list['State'] == 'InService':
        counter = counter + 1

print("There are " + str(counter) + " instances in " + lbname)
if counter == 3:
    print("All instances are online! we can start deploy !")
    # check if app1 status is up
    if check_status('i-02aa1098e70254776') == 'InService':
        print("i-02aa1098e70254776 is InService continue !")
    else:
        exit()
    # run chef on app1

    #check if app1 status is up
    if check_status('i-02aa1098e70254776') not in 'InService':
        print("i-02aa1098e70254776 is not in service - exit !")
        exit()
    while check_status('i-02aa1098e70254776') == 'InService':
        print("i-02aa1098e70254776 is InService - in DEPOLY-  going to sleep 4 seconds..")
        sleep(4)
    #check if app1 status is down
    while check_status('i-02aa1098e70254776') == 'OutOfService':
        print("i-02aa1098e70254776 is in OutOfService - in DEPOLY .. going to sleep 5 seconds..")
        sleep(5)
    # check if app1 status is up
    if check_status('i-02aa1098e70254776') == 'InService':
        print("i-02aa1098e70254776 is InService - DEPOLY Completed ! Continue to next app")

else:
    print("Goodbye - not all instances are up!")
    exit()


