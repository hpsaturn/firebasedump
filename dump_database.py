import json
import firebase_admin
from firebase_admin import db
from datetime import datetime


cert = 'kcanariesdb-firebase-admin.json'
dbpath = 'https://kcanariesdb.firebaseio.com/'


cred = firebase_admin.credentials.Certificate(cert)
firebase_admin.initialize_app(cred, {'databaseURL': dbpath})

try:
  now = datetime.now().strftime("%Y%m%d%H%M%S")
  output = 'canairio'+str(now)+'.json'
  with open(output, 'w') as cf:
      cf.write(json.dumps(db.reference('/tracks_info').get()))
except:
    raise IOError('Error in saving data to file!!\n')
