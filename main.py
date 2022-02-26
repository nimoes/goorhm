#!/usr/bin/python3
"""
aws boto play
"""

import boto3
import botocore
import os
import sys


ec2 = boto3.resource('ec2', region_name='us-east-1')

snapshots = ec2.snapshots.all()

count = 0
for s in snapshots:
    count += 1
    print(f'Snapshot {s.id} for volume {s.volume_id}')

print(count)

