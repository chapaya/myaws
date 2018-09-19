'''
[root@utils2 ~]# python matos.py US eranLB
'''

import boto3
import os
from time import sleep
import sys
import logging

# ENV = IR/US
env = sys.argv[1]
# lbname = LB1/LB2/LB3
lbname = sys.argv[2]
identity_file = ''

if env == 'IR':
    identity_file = '~/.ssh/ir.pem'
    region = 'eu-west-1'
elif env == 'US':
    identity_file = '~/myaws.pem'
    region = 'us-east-1'
elif env == 'xxx':
    identity_file = '~/.ssh/vir.pem'
    region = 'us-east-1'

ec2client = boto3.client('ec2', region_name=region)
ec2resource = boto3.resource('ec2', region_name=region)
elb = boto3.client('elb', region_name=region)

print(env)
print(identity_file)
print(region)

def get_app_list(lbname):
    """
    :param lbname: Get Balancer name
    :return: list of servers in elb
    """
    server_list = []
    lbs = elb.describe_load_balancers(LoadBalancerNames=[lbname, ], )
    for lb in lbs['LoadBalancerDescriptions']:
        for server in lb['Instances']:
            server_list.append(server['InstanceId'])
    return server_list


def get_name(fid):
    """
    :param fid: Get ec2 id
    :return: server name according to Name Tag
    """
    ec2instance = ec2resource.Instance(fid)
    instancename = ''
    for tags in ec2instance.tags:
        if tags["Key"] == 'Name':
            instancename = tags["Value"]
    return instancename


def get_app_status(appid):
    """
    :param appid: Get ec2 server id
    :return: return up or down ( and exit code 1)
    """
    res = elb.describe_instance_health(LoadBalancerName=lbname, Instances=[{'InstanceId': appid}, ])
    appstat = (res['InstanceStates'][0]['State'])
    return appstat

def is_lb_min2(lbname):
    """
    :param lbname:
    :return: return true if there are 2 instances inservice
    """
    count = 0
    list = get_app_list(lbname)
    for server in list:
        print(get_app_status(server))
        if get_app_status(server) in "InService":
            count = count + 1
            print(count)
    if count > 2:
        print(str(count) + " bigger than 2 - Return True")
        return True
    else:
        print(str(count) + " less than 2 - Return False")
        return False


def which_user(appid):
    """
    :param appid:
    :return: the relevant user : centos or ec2-user
    """
    # check which user
    # centos = 'ImageId': 'ami-0d139608ed218ae97',
    response = ec2client.describe_instances(InstanceIds=[appid, ], )
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            #print(instance['ImageId'])
            ami = (instance['ImageId'])
            #print(ami)

    #ami-0d139608ed218ae97 - emea centos
    #ami-783a2107 - US centos
    #eran ami-9887c6e7
    #if (ami == 'ami-0d139608ed218ae97') or (ami == 'ami-783a2107'):
    if (ami == 'ami-9887c6e7'):
        user = 'centos'
    else:
        user = 'ec2-user'
    print(user)
    return user

def run_chef_client(appname,appid):
    """
    :param appid:
    :return:
    """
    ssh_user = which_user(appid)
    print(ssh_user)
    #ssh = os.system("ssh -t -t -i %s -n -o StrictHostKeyChecking=no %s@%s 'sudo chef-client'" % (
    ssh = os.system("ssh -t -t -i %s -n -o StrictHostKeyChecking=no %s@%s 'sudo service nginx stop'" % (
    identity_file, ssh_user, appname))
    print(ssh)
    print("run chef-client")


# Main program #
def main():
    logging.basicConfig(filename='deploy_matos.log', level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    logging.info('Main program started')
    print("ELB status : " + lbname)
    list = get_app_list(lbname)
    print(list)
    sleep(5)
    for appid in list:
        appname = get_name(appid)
        print(appid + " - " + appname + " Starting ... !")
        print(appid + " - " + get_name(appid) + " - " + get_app_status(appid))
        while True:
            sleep(3)
            if is_lb_min2(lbname):
                logging.info('Run chef_client')
                logging.info(appname)
                run_chef_client(appname, appid)
                while True:
                    # loop wait till app will be OutOfService
                    print(appname)
                    print(appid)
                    res = elb.describe_instance_health(LoadBalancerName=lbname, Instances=[{'InstanceId': appid}, ])
                    appstat = (res['InstanceStates'][0]['State'])
                    print(appid + " - " + appstat)
                    if appstat in 'InService':  # Wait to be OutOfService
                        print(appid + " - " + appname + " is InService .. sleep 10 seconds ...")
                        logging.info('Wait to be OutOfService ... Sleep 5 ...')
                        sleep(5)
                    else:
                        print(appid + " - " + appname + " is OutOfService.. Continue to next app")
                        logging.info('Continue to next app')
                        sleep(3)
                        break
            else:
                print("There are 2 active servers in LB .. going to sleep 5 seconds ...")
                sleep(5)
                while True: # wait till is_lb_min2(lbname) is true
                    if not is_lb_min2(lbname) :
                        print("is lb min 2 is false ...sleep 3..")
                        sleep(3)
                    else:
                        print("There are 3 apps in service .. continue..")
                        print("Running chef-client on " + appname)
                        run_chef_client(appname, appid)
                        print("chef-client run on " + appname)
                        sleep(10)
                        break
            break

    logging.info('Program ended !')
    print('Program ended !')



if __name__ == "__main__":
    main()
