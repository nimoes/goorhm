#!/usr/bin/python3
"""
aws boto play
"""

import boto3
import botocore
import argparse
import sys


def login_check(region):
    sess = boto3.Session()
    client = boto3.client('sts', region_name=region)

    try:
        arn = client.get_caller_identity()['Arn']
        print("Your profile:\t" + str(arn))
    except botocore.exceptions.ClientError as error:
        sys.exit("couldn't retrieve account info")
    
    return


if __name__ == '__main__':
    # add args
    parser = argparse.ArgumentParser(description="Based on specified region,\
        the program will return a list of public EBS in json", \
            epilog="python ")
    parser.add_argument("-r", "--region", required=True, type=str, \
         help="specify region (\"us-west-1\")")
    parser.add_argument("--preview", required=False, action='store_true', \
        help="prints first 10 entries")

    # parse args
    args = parser.parse_args()
    REGION_NAME = args.region
    PREVIEW = True if args.preview else False

    # call function
    login_check(REGION_NAME)