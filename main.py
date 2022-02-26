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
        print(f'Snapshots id {s.id} for volume {s.volume_id} encrypted: {s.encrypted}')

    print(count)

ec2 = boto3.resource('ec2', region_name='us-east-1')
snapshots = ec2.snapshots.limit(10)

onlyEncrypted = snapshots.filter(Filters=[{'Name':'encrypted', 'Values':['true']}])
printResults(onlyEncrypted)


