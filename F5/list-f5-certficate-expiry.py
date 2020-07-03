#!/usr/bin/env python3

import sys
from argparse import ArgumentParser
from getpass import getpass
from datetime import datetime, timezone
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta
from f5.bigip import ManagementRoot

parser = ArgumentParser()
parser.add_argument('--f5-ltm', required=True, help='ip address of fqdn of f5 ltm')
parser.add_argument('--username', default='admin', help='username defaults to admin')
parser.add_argument('--password', default='foobar', help="password for user (default to prompt user)")
parser.add_argument('--threshold', default=6, type=int, help='no of weeks before cert expiry defaults to 6')
args=parser.parse_args()

if (args.password == 'foobar' or args.password == ''):
  args.password = getpass()

try:
  mgmt = ManagementRoot(args.f5_ltm, args.username, args.password)
except Exception as e:
  print('Opps!, Something went wrong, below is the error')
  print(e)
  sys.exit(1)

today = datetime.now(timezone.utc)
nearFuture = today+relativedelta(weeks=+args.threshold)

print("Certificate Path,Valid until,Status")
for cert in mgmt.tm.sys.file.ssl_certs.get_collection():
  expiry = parse(cert.expirationString)

  if expiry <= today:
    print("'{}','{}','Expired'".format(
      cert.fullPath,
      expiry.astimezone(),
    ))
  elif (expiry > today and expiry <= nearFuture):
    print("'{}','{}','Expiring soon'".format(
      cert.fullPath,
      expiry.astimezone(),
    ))
  else:
    print("'{}','{}','Valid'".format(
      cert.fullPath,
      expiry.astimezone(),
    ))

