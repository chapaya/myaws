import boto3
#http://www.pythonexample.com/search/aws-boto3-ec2/2

region_list = ['us-east-1']

for region in region_list:
    print('REGION:', region)
    ec2 = boto3.resource('ec2', region)
    for instance in ec2.instances.all():
        print('instance:',instance)
        ec2tags = instance.tags
        print('tags:', ec2tags)
        for volume in instance.volumes.all():
            print('volume:', volume)
            #           Create tags on volume if they don't match the instance
            if volume.tags != ec2tags:
                print('\033[93m' + 'Tags don\'t match, updating')
                #volume.create_tags(DryRun=False, Tags=ec2tags)
            print('tags:', volume.tags)