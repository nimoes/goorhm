#!/usr/bin/python3
"""
aws boto play
"""

import boto3
import botocore
import os
import sys


def login_check(call, REGION_NAME='us-east-1'):
    call='sts'
    sess = boto3.Session()
    client = boto3.client(call, region_name=REGION_NAME)

    try:
        arn = client.get_caller_identity()['Arn']
        return(arn)
    except botocore.exceptions.ClientError as error:
        sys.exit("couldn't retrieve account info")

def main():
    login_check()
    return

if __name__ == '__main__':
    main()