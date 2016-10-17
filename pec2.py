import boto3
import os

client = boto3.client('ec2')
instances = client.describe_instances()
#pprint.pprint(instances['Reservations'])
for instance in instances['Reservations']:
   instanceId = instance['Instances'][0]['InstanceId']
   #print instanceId
   
   ###################################################
   ###
   ###  Disable API Protection
   ###
   ###################################################
   #response = client.modify_instance_attribute(
   #    InstanceId = instanceId,
   #    Attribute='disableApiTermination',
   #    Value = 'false')
   #print response

   ###################################################
   ###
   ###  Delete all the instances
   ###
   ###################################################
   response = client.terminate_instances(
       InstanceIds=[instanceId]
       )

   print response
