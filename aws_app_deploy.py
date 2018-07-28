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

# Check elb status
res = elb.describe_instance_health(
    LoadBalancerName=lbname
    )

def app_deploy(appid):
#app
    # check if app status is up
    appname = get_name(appid)
    print(appname)
    res = elb.describe_instance_health(LoadBalancerName=lbname, Instances=[{'InstanceId': appid}, ])
    appstat = (res['InstanceStates'][0]['State'])
    print(appid + " - " + appstat)
    if appstat in 'InService':
        print(appid + " - " + appname + " is up - Deploy Started ...")
    else:
        print(appid + " - " + appname + " is not up - Goodbye!")
        exit()

    # Run chef-client on app

    # Wait for app to be OOS
    while True:
        res = elb.describe_instance_health(LoadBalancerName=lbname, Instances=[{'InstanceId': appid}, ])
        appstat = (res['InstanceStates'][0]['State'])
        print(appid + " - " + appname + " - " + appstat)
        if appstat in 'InService':
            print(appid + " - " + appname + " is still up .. sleep 3 seconds ...")
            sleep(3)
        else:
            print(appid + " - " + appname + " is OOS ..")
            break

    # Wait for app to be InService
    while True:
        res = elb.describe_instance_health(LoadBalancerName=lbname, Instances=[{'InstanceId': appid}, ])
        appstat = (res['InstanceStates'][0]['State'])
        print(appid + " - " + appstat)
        if appstat in 'OutOfService':
            print(appid + " - " + appname + " is OutOfService .. sleep 3 seconds ...")
            sleep(3)
        else:
            print(appid + " - " + appname + " is in service ..")
            sleep(3)
            break

    res = elb.describe_instance_health(LoadBalancerName=lbname, Instances=[{'InstanceId': appid}, ])
    appstat = (res['InstanceStates'][0]['State'])
    print(appid + "-" + appname + " status " + appstat)
    print(appid + "-" + appname + " deployed !")

# Start
# Check elb status
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

# Deploy started
    app_deploy(app1id)
    app_deploy(app2id)
    app_deploy(app3id)

    print("Deploy completed !")


else:
    print("Goodbye - not all instances are up!")
    exit()