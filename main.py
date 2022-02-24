#!/usr/bin/python3
"""
aws boto play
"""

import boto3
import botocore
import os
import sys

client = boto3.client('sts', region_name='us-east-1')

try:
    account_info = client.get_caller_identity().get('Arn')
except botocore.exceptions.ClientError as error:
    sys.exit("couldn't retrieve account info")