"""
firebasedump -- utility for dump data from Firebase database

Usage:
  firebasedump  (-d <database> -c <credentials>) <dbtarget> 
  firebasedump  [--verbose] (-d <database> -c <credentials>) <dbtarget> [<output>]
  firebasedump -h | --help
  firebasedump -v | --version

Options:
  -h --help                     Show help screen.
  -v --version                  Show version.
  -d db, --database db          Url path of your database
  -c cd, --credentials cd       Path of your credentials (json file)
  -s, --verbose                 Enable logs
  dbtarget                      Database target path for dump i.e: /users

"""

import json
import sys
import firebase_admin
from firebase_admin import db
from datetime import datetime
from docopt import docopt


def dumpdb(target, output):

  now = datetime.now().strftime("%Y%m%d%H%M%S")

  if output == None:
    out = str(target).replace('/', '')
    out = out+str(now)+'.json'
  else:
    out = output+str(now)+'.json'

  try:
    with open(out, 'w') as cf:
        cf.write(json.dumps(db.reference(target).get()))
  except:
      raise IOError('Error in saving data to file!!\n')


if __name__ == '__main__':
  arguments = docopt(__doc__, version='0.0.1')
  debugmode = arguments["--verbose"]
  cert = arguments["--credentials"]
  dbpath = arguments["--database"]
  target = arguments["<dbtarget>"]
  output = arguments["<output>"]

  if debugmode:
    print(arguments)

  # Firebase database init
  cred = firebase_admin.credentials.Certificate(cert)
  firebase_admin.initialize_app(cred, {'databaseURL': dbpath})

  dumpdb(target, output)
