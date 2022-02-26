#!/usr/bin/python3
"""
aws boto play
"""

import boto3
import botocore
import argparse
import sys
import logging
import re


def login_check(region) -> str:
    """
    check user's authentication and print user's authenticated profile
    """
    client = boto3.client('sts', region_name=region)

    try:
        arn = client.get_caller_identity()['Arn']
        account_id = client.get_caller_identity()['Account']
        logger.info("Your current profile:\t" + str(arn))
    except botocore.exceptions.ClientError as error:
        sys.exit("couldn't retrieve account info")
    
    return account_id


def ebsList(aws_account_id, reg):
    """
    enumerate ebs in region
    """

    ec2 = boto3.resource('ec2', region_name=reg)

    # list publicly available unencrypted snapshots
    snapshots = ec2.snapshots.limit(count=1).filter(
        MaxResults=10,
        Filters = [
            {
                'Name': 'owner_id',
                'Values': [aws_account_id],
            },
            {
                'Name': 'encrypted',
                'Values': ['false'],
            },
        ],
    )

    # for ss in snapshots:
    #     print(dir(ss))
    #     print("owner_id" + str(ss.owner_id))
    #     print("\nowner_alias" + str(ss.owner_alias))
    #     print("\nstate" + str(ss.state))
    #     print("\nstart_time" + str(ss.start_time))
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

    # logger
    logger = logging.getLogger('EBS Snapshots Enumerator')
    logger.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # add formatter to ch
    ch.setFormatter(formatter)

    # add ch to logger
    logger.addHandler(ch)

    # check if authentication is successful, returns account id
    aws_account_id = login_check(REGION_NAME)

    logger.info("Checking for vulnerable EBS snapshots...")

    if aws_account_id:
        ebsList(aws_account_id, REGION_NAME)
    else:
        sys.exit(1)
    