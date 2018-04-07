import boto3
ec2 = boto3.resource('ec2', region_name='us-east-1')
ec2cl = boto3.client('ec2', region_name='us-east-1')

volumes = ec2.volumes.all()
vol = 'vol-0dd8de038a3c9f8c3'

print(volumes)
for v in volumes:
    print(v.id) # all volumes
    print(v)
'''
ec2.Volume(id='vol-0dd8de038a3c9f8c3')
vol-0767bf1f003dbfa2a
ec2.Volume(id='vol-0767bf1f003dbfa2a')
vol-0158c8e11d031bb9d
'''
print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
volumes = ec2.volumes.filter(Filters=[{'Name': 'status', 'Values': ['available']}]) # if you want to list only available disks - not connected
for v in volumes:
    #print(v.id) # all volumes
    print("This disk is avalible " + v.id)
    # Delete the disk
    #response = ec2cl.delete_volume(
    #    VolumeId=v.id,
    #)
    #print(response)

    '''
    This disk is avalible vol-0efca32aee2ab7574
'''

print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
response = ec2cl.describe_volume_status(
    VolumeIds=[
        'vol-0efca32aee2ab7574',
    ],
)
print(response)

print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
response = ec2cl.describe_volumes()
print(response)
for row in response['Volumes']:
    #print(row[VolumeId])
    print("vol_id:" + str(row['VolumeId']) ,"vol_size_in_GB:" + str(row['Size']) ,"Vol_type:" + str(row['VolumeType']) ,"vol_state:" + str(row['State']))
    #    print(row['VolumeId'] , row['Size'] , row['VolumeType'] , row['State'])
'''
vol_id:vol-0ed1db6aa8d46f88b vol_size_in_GB:8 Vol_type:gp2 vol_state:in-use
vol_id:vol-078856ed07259a86d vol_size_in_GB:8 Vol_type:gp2 vol_state:in-use
vol_id:vol-0efca32aee2ab7574 vol_size_in_GB:8 Vol_type:gp2 vol_state:available
vol_id:vol-08dc3aaccb501c8c3 vol_size_in_GB:8 Vol_type:gp2 vol_state:in-use
vol_id:vol-0fa6413a25220bc3c vol_size_in_GB:8 Vol_type:gp2 vol_state:in-use
'''