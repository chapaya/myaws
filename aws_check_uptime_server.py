#check if server up more than 1 day
import boto3
import datetime
from dateutil import parser
ec2client = boto3.client('ec2')
ec2resource = boto3.resource('ec2')

def get_name(fid):
    ec2instance = ec2resource.Instance(fid)
    instancename = ''
    for tags in ec2instance.tags:
        #print(tags) # print all tags
        if tags["Key"] == 'Name':
            instancename = tags["Value"]
    return(instancename)

response = ec2client.describe_instances()

for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        strchk = "myserver"
        servername=str(get_name(fid=instance["InstanceId"]))
        if strchk in servername:
           #print("Instance_id=" + instance["InstanceId"] + " Name=" + get_name(fid=instance["InstanceId"]) + " Lunchtime:" + str(instance["LaunchTime"]))
           current_time = (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
           #print(current_time)
           luntime = str(instance["LaunchTime"])
           #print(luntime)
           luntime1 = parser.parse(luntime)
           launchtime_naive = luntime1.replace(tzinfo=None)
           then = datetime.datetime.utcnow() + datetime.timedelta(days = -1)
           if launchtime_naive < then:
               print("NOT OK - " + get_name(fid=instance["InstanceId"]) + " -" + " Lunchtime: " + str(instance["LaunchTime"]) + " run more than a day !")
               print("EC2 lunch time: " + str(luntime1))
               print("One day ago time: " + str(then))
           else:
               print("OK - " + get_name(fid=instance["InstanceId"]) + " -" + " Lunchtime: " + str(instance["LaunchTime"]) + " run less than a day")
               print("EC2 lunch time: " + str(luntime1))
               print("One day ago time: " + str(then))
           print("------------------------------------------------------------------------------------------------------------------------")
        else:
           x=1
