# goorhm
inspired by dc19 on public ebs, this program will check if your assets are exposed

## Setup
### Windows (PS)
```
> cd goorhm
> python3 -m venv venv
> .\venv\Scripts\activate
> pip install -r requirements.txt

```

### Linux (Ubuntu) / MacOS
```
> cd goorhm
> python3 -m venv venv
> source ./venv/bin/activate
> pip install -r requirements.txt
```

## Usage
```
> python ebspose.py -h
usage: ebspose.py [-h] -r REGION [--preview]

Based on specified region, the program will return a list of public EBS in json

optional arguments:
  -h, --help            show this help message and exit
  -r REGION, --region REGION
                        specify region ("us-west-1")
  --preview             prints first 10 entries
  -o OUTPUT, --output OUTPUT
                        name of the output json file
```

```
> python ebspose.py -r "us-east-1" -o myoutput --preview

2022-02-26 17:22:38,468 - EBS Snapshots Enumerator - INFO - Your current profile:       arn:aws:iam::621121731539:user/dev-boto3
2022-02-26 17:22:38,470 - EBS Snapshots Enumerator - INFO - Checking for your vulnerable EBS snapshots...
2022-02-26 17:22:38,569 - EBS Snapshots Enumerator - INFO - Retrieved EBS
2022-02-26 17:22:38,815 - EBS Snapshots Enumerator - INFO - Printing a preview of output
2022-02-26 17:22:38,816 - EBS Snapshots Enumerator - INFO - [('snap-081170e1eb6038193', {'tags': [{'Key': 'description', 'Value': 'dummyebs'}], 'aws_account_id': '621121731539', 'volume_id': 'vol-0accb1e4743bee2bf', 'backup_time': datetime.datetime(2022, 2, 26, 20, 7, 42, 673000, tzinfo=tzutc())})]
2022-02-26 17:22:38,818 - EBS Snapshots Enumerator - INFO - Your output file has been generated
```