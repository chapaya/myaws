from time import sleep

import boto3
ec2clor = boto3.client('ec2', region_name='us-east-1')
ec2resor = boto3.resource('ec2', region_name='us-east-1')
elb = boto3.client('elb', region_name='us-east-1')
### elb values ###
lbname='lb3'
app1id='i-02aa1098e70254776'
app2id='i-0b3a5f7fb05e65b13'
app3id='i-0d95ae1e4c01fa45c'
##################

def get_name(fid):
    ec2instance = ec2resor.Instance(fid)
    instancename = ''
    for tags in ec2instance.tags:
        if tags["Key"] == 'Name':
            instancename = tags["Value"]
    return(instancename)

res = elb.describe_instance_health(
    LoadBalancerName=lbname
    )

counter=0
print("Here is the instances status for load balancer: " + lbname)
for ec2list in res['InstanceStates']:
    print("InstanceId: " + ec2list['InstanceId'] + " - " + get_name(fid=ec2list['InstanceId']) + " - " + ec2list['State'])
    if ec2list['State'] == 'InService':
        counter = counter + 1

print("There are " + str(counter) + " InService instances in " + lbname)
if counter == 3:
    print("All instances are online! we can start deploy !")

# app1
    # check if app1 status is up
    print("Starting app1 " + app1id)
    res = elb.describe_instance_health(LoadBalancerName=lbname, Instances=[{'InstanceId': app1id}, ])
    app1stat=(res['InstanceStates'][0]['State'])
    print(app1stat)
    if app1stat in 'InService':
        print("app1 is up - Deploy Started ...")
    else:
        print("app1 is not up - Goodbye!")
        exit()

    # Run chef-client on app1

    # Wait for app1 to be OOS
    while 1:
        res = elb.describe_instance_health(LoadBalancerName=lbname, Instances=[{'InstanceId': app1id}, ])
        app1stat = (res['InstanceStates'][0]['State'])
        print(app1id + " -" + app1stat)
        if app1stat in 'InService':
            print("app1 is till up .. sleep 3 seconds ...")
            sleep(3)
        else:
            print("app1 is OOS ..")
            break

    # Wait for app1 to be OOS
    while 1:
        res = elb.describe_instance_health(LoadBalancerName=lbname, Instances=[{'InstanceId': app1id}, ])
        app1stat = (res['InstanceStates'][0]['State'])
        print(app1id + " -" + app1stat)
        if app1stat in 'OutOfService':
            print("app1 is OutOfService .. sleep 3 seconds ...")
            sleep(3)
        else:
            print("app1 is in service ..")
            sleep(3)
            break

    res = elb.describe_instance_health(LoadBalancerName=lbname, Instances=[{'InstanceId': app1id}, ])
    app1stat = (res['InstanceStates'][0]['State'])
    print("app1 status " + app1id + app1stat)
    print("app1 deployed !")


#app2
    ### Continue to app2 ###
    # check if app2 status is up
    res = elb.describe_instance_health(LoadBalancerName=lbname, Instances=[{'InstanceId': app2id}, ])
    app2stat = (res['InstanceStates'][0]['State'])
    print(app2id + " -" + app2stat)
    if app2stat in 'InService':
        print("app2 is up - Deploy Started ...")
    else:
        print("app2 is not up - Goodbye!")
        exit()

    # Run chef-client on app2

    # Wait for app2 to be OOS
    while 1:
        res = elb.describe_instance_health(LoadBalancerName=lbname, Instances=[{'InstanceId': app2id}, ])
        app1stat = (res['InstanceStates'][0]['State'])
        print(app2id + " -" + app2stat)
        if app1stat in 'InService':
            print("app2 is till up .. sleep 3 seconds ...")
            sleep(3)
        else:
            print("app2 is OOS ..")
            break

    # Wait for app2 to be OOS
    while 1:
        res = elb.describe_instance_health(LoadBalancerName=lbname, Instances=[{'InstanceId': app2id}, ])
        app2stat = (res['InstanceStates'][0]['State'])
        print(app2id + " -" + app2stat)
        if app2stat in 'OutOfService':
            print("app2 is OutOfService .. sleep 3 seconds ...")
            sleep(3)
        else:
            print("app2 is in service ..")
            sleep(3)
            break

    res = elb.describe_instance_health(LoadBalancerName=lbname, Instances=[{'InstanceId': app2id}, ])
    app1stat = (res['InstanceStates'][0]['State'])
    print("app2 status " + app2stat)
    print("app2 deployed !")

## app3

    # check if app3 status is up
    print("Starting app3 " + app3id)
    res = elb.describe_instance_health(LoadBalancerName=lbname, Instances=[{'InstanceId': app3id}, ])
    app3stat = (res['InstanceStates'][0]['State'])
    print(app3stat)
    if app3stat in 'InService':
        print("app3 is up - Deploy Started ...")
    else:
        print("app3 is not up - Goodbye!")
        exit()

    # Run chef-client on app3

    # Wait for app3 to be OOS
    while 1:
        res = elb.describe_instance_health(LoadBalancerName=lbname, Instances=[{'InstanceId': app3id}, ])
        app3stat = (res['InstanceStates'][0]['State'])
        print(app3id + " -" + app3stat)
        if app3stat in 'InService':
            print("app3 is till up .. sleep 3 seconds ...")
            sleep(3)
        else:
            print("app3 is OOS ..")
            break

    # Wait for app3 to be OOS
    while 1:
        res = elb.describe_instance_health(LoadBalancerName=lbname, Instances=[{'InstanceId': app3id}, ])
        app3stat = (res['InstanceStates'][0]['State'])
        print(app3id + " -" + app3stat)
        if app3stat in 'OutOfService':
            print("app3 is OutOfService .. sleep 3 seconds ...")
            sleep(3)
        else:
            print("app3 is in service ..")
            sleep(3)
            break

    res = elb.describe_instance_health(LoadBalancerName=lbname, Instances=[{'InstanceId': app3id}, ])
    app3stat = (res['InstanceStates'][0]['State'])
    print("app3 status " + app3id + app3stat)
    print("app3 deployed !")
    print("Deploy completed !")

else:
    print("Goodbye - not all instances are up!")
    exit()