#!/usr/bin/python3
"""
aws boto play
"""

import boto3
import botocore
import argparse
import sys
import logging
import json


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


def ebsList(aws_account_id, reg, preview=False) -> dict:
    """
    enumerate ebs based on specified region
    """

    ec2 = boto3.resource('ec2', region_name=reg)

    # list publicly available unencrypted snapshots
    # if preview flag was used, print up to 10 entries in the console
    count = 10 if preview == True else 0

    snapshots = ec2.snapshots.all().filter(
        Filters = [
            {
                'Name': 'owner-id',
                'Values': [aws_account_id],
            },
            {
                'Name': 'encrypted',
                'Values': ['false'],
            },
        ],
    )
    
    # if snapshot exists, print message
    if snapshots:
        logger.info("Retrieved EBS")
    else:
        logger.info("No vulnerable EBS found under this region")
    
    d= {}

    # prep output
    for ss in snapshots:
        d[ss.id] = {}
        d[ss.id]['tags'] = ss.tags
        d[ss.id]['aws_account_id'] = ss.owner_id
        d[ss.id]['volume_id'] = ss.volume_id
        d[ss.id]['backup_time'] = ss.start_time
    
    # if preview flag was used, print a preview with up to 10 entries
    if preview:
        logger.info("Printing a preview of output")
        logger.info(list(d.items())[:count])

    return d


if __name__ == '__main__':
    # add args
    parser = argparse.ArgumentParser(description="Based on specified region,\
        the program will return a list of public EBS in json", \
            epilog="python ")
    parser.add_argument("-r", "--region", required=True, type=str, \
         help="specify region (\"us-west-1\")")
    parser.add_argument("--preview", required=False, action='store_true', \
        help="prints first 10 entries")
    parser.add_argument("-o", "--output", required=False, help="name of the \
        output json file")

    # parse args
    args = parser.parse_args()
    REGION_NAME = args.region
    PREVIEW = True if args.preview else False
    OUTPUT = args.output

    # logger
    logger = logging.getLogger('EBS Snapshots Enumerator')
    logger.setLevel(logging.DEBUG)
    # console handler
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # add formatter to console handler
    ch.setFormatter(formatter)
    # add console event handler to logger
    logger.addHandler(ch)


    # check if authentication is successful, returns account id
    aws_account_id = login_check(REGION_NAME)

    logger.info("Checking for your vulnerable EBS snapshots...")

    if aws_account_id:
        ebs_output = ebsList(aws_account_id, REGION_NAME, PREVIEW)
    else:
        sys.exit(1)
    
    # save output, if specified
    if OUTPUT:
        ff = str(OUTPUT)+'.json'
        with open(ff, 'w') as f:
            json.dump(ebs_output, f, default=str)
        logger.info("Your output file has been generated")