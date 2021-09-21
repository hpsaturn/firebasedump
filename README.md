# CanAirIO Realtime Database #

This README would normally document whatever steps are necessary to get your application up and running.

## Database Structure

The database has three data schemas:

**tracks_info**: Info of current devices. Each device endpoint has the sessions ids of each tracking without the data of track. This data is in track_data.  

**tracks_data**: With the same endpoint that track_info, this path in firebase has the all data of each track session.  

**tracks_ctrl**: With this endpoint we have the control to set the interval time or enable/disable the background service.

# Python API

## Prerequisites

- GNU Linux or compatible OS
- Python3

## Installation Firebase Admin

Please first install on a python virtual env, `firebase_admin`

```bash
python3 -m venv venv
cd venv/ && source bin/activate
python -m pip install --upgrade setuptools
pip install -U pip
pip install firebase_admin
```

## Testing connection

For example in `ipython` or Python `console` test it:

```python
import firebase_admin
from firebase_admin import db
cred = firebase_admin.credentials.Certificate('kcanariesdb-firebase-admin.json')
firebase_admin.initialize_app(cred,{'databaseURL':'https://kcanariesdb.firebaseio.com/'})
```

Output:

```python
<firebase_admin.App at 0x7f0a9fdcb1d0>
```

For more information [here](https://firebase.google.com/docs/admin/setup#python)

## Retrive devices info

On `track_info` have the list of devices without data of tracking, only the info of each track session of each device:

```python
ref = db.reference('/tracks_info')
print(ref.get())
```

## Retrive device data

With a some `deviceId` from `tracks_info` you can retrive the tracking that of device:

```python
ref = db.reference('/track_data/b25b006ef2da3748')
print(ref.get())
```

