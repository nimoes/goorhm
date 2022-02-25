# goorhm
inspired by dc19 on public ebs, this program will check if your assets are exposed

## Setup
### Windows (PS)
```
> mkdir goorhm
> cd goorhm
> python3 -m venv venv
> .\venv\Scripts\activate
> pip install -r requirements.txt

```

### Linux (Ubuntu) / MacOS
```
> mkdir goorhm
> cd goorhm
> python3 -m venv venv
> source ./venv/bin/activate
> pip install -r requirements.txt
```

## Usage
```
> python main.py -h
usage: main.py [-h] -r REGION [--preview]

Based on specified region, the program will return a list of public EBS in json

optional arguments:
  -h, --help            show this help message and exit
  -r REGION, --region REGION
                        specify region ("us-west-1"
  --preview             prints first 10 entries
```