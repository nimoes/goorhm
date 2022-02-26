#!/usr/bin/python3
"""
aws boto play
"""


import boto3
import botocore
import os
import sys

def printResults(snapshots):
    count = 0
    for s in snapshots:
        count += 1
        print(f'Snapshots id {s.id} for volume {s.volume_id} encrypted: {s.encrypted} owner id: {s.owner_id} volume size: {s.volume_size}')

    print(count)

client = boto3.client('sts', region_name='us-east-1')
account_info = client.get_caller_identity()['Account']


ec2 = boto3.resource('ec2', region_name='us-east-1')

print(account_info)
print(type(account_info))


onlyEncrypted = ec2.snapshots.limit(count=100).filter(
    Filters = [
        {
            'Name':'encrypted',
            'Values':['12345']
        }
    ]
)
printResults(onlyEncrypted)




