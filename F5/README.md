# List F5 SSL certificate status
This script `` lists all certificates hosted on F5 ltm and their status

## Usage
IP address or fqdn of F5 management interface is mandatory. If username and passwords are not provided it will default to admin and prompt for password.  The threshold period for verifying certificates defaults to 6 weeks, optionally you can modify this with the --threshold argument.

```
usage: list-f5-certficate-expiry.py [-h] --f5-ltm F5_LTM [--username USERNAME] [--password PASSWORD]
                                    [--threshold THRESHOLD]

optional arguments:
  -h, --help            show this help message and exit
  --f5-ltm F5_LTM       ip address of fqdn of f5 ltm
  --username USERNAME   username defaults to admin
  --password PASSWORD   password for user (default to prompt user)
  --threshold THRESHOLD
                        no of weeks before cert expiry defaults to 6
```

## Setup Instructions
Requires python version 3, can be used with or without virtual environment.  Please download the script and requirements.txt 

To install the dependent modules please run `pip install -r requirements.txt` in your environment.  On some systems you might need to invoke pip3 instead of pip


