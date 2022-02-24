#!/usr/bin/python3
"""
aws boto play
"""

import boto3
import botocore
import os
import sys
'''
ec2 = boto3.client('ec2',region_name='us-east-1')
response = ec2.describe_instances()
print(response)
'''



client = boto3.client('sts', region_name='us-east-1')

try:
    account_info = client.get_caller_identity()['Arn']
    print(account_info)
except botocore.exceptions.ClientError as error:
    sys.exit("couldn't retrieve account info")

