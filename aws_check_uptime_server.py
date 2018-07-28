import boto3
import datetime
from dateutil import parser
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

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

body = []
send_mail= 0
response = ec2client.describe_instances()

for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        strchk = "myserver_name"
        servername=str(get_name(fid=instance["InstanceId"]))
        if strchk in servername:
           #print("Instance_id=" + instance["InstanceId"] + " Name=" + get_name(fid=instance["InstanceId"]) + " Lunchtime:" + str(instance["LaunchTime"]))
           current_time = (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
           luntime = str(instance["LaunchTime"])
           luntime1 = parser.parse(luntime)
           launchtime_naive = luntime1.replace(tzinfo=None)
           then = datetime.datetime.utcnow() + datetime.timedelta(days = -1)
           if launchtime_naive < then:
               print("Server " + get_name(fid=instance["InstanceId"]) + " -" + " Lunchtime: " + str(instance["LaunchTime"]) + " run more than a day !")
               str1 = ("Server - " + get_name(fid=instance["InstanceId"]) + " -" + " Lunchtime: " + str(instance["LaunchTime"]) + " run more than a day !")
               body.append(str1)
               print("EC2 lunch time: " + str(luntime1))
               print("One day ago time: " + str(then))
               send_mail = 1
           else:
               print("OK - " + get_name(fid=instance["InstanceId"]) + " -" + " Lunchtime: " + str(instance["LaunchTime"]) + " run less than a day")
           print("------------------------------------------------------------------------------------------------------------------------")
        else:
           x=1

body1 = ('\n'.join(body))
print(body1)

# Mail setup
if send_mail == 1:
   server = smtplib.SMTP('xxxxx')
   fromaddr = "xxxxxm"
   toaddr = "xxxx"
   msg = MIMEMultipart('alternative')
   msg['Subject'] = "server EC2 - up more than a day"
   msg['From'] = fromaddr
   msg['To'] = toaddr
   msg.attach(MIMEText(body1, 'plain'))
   text = msg.as_string()
   server.sendmail(fromaddr, toaddr, text)
   server.quit()
else:
   print("All OK ! No mail !")
