#!/usr/bin/python

import argparse
import httplib2
import os
import sys
import json

from apiclient import discovery
from oauth2client import file
from oauth2client import client
from oauth2client import tools

parser = argparse.ArgumentParser(
    description=__doc__,
    formatter_class=argparse.RawDescriptionHelpFormatter,
    parents=[tools.argparser])

BUCKET_NAME = 'mm-dev-2'
SECRET_NAME = 'client_secret.json'

client_secret = os.path.join(os.getcwd(), SECRET_NAME)
auth_flow = client.flow_from_clientsecrets(
    client_secret,
    scope='https://www.googleapis.com/auth/devstorage.read_only',
    message=tools.message_if_missing(client_secret))


def main():
    args = parser.parse_args()
    storage = file.Storage('../credentials.dat')
    credentials = storage.get()
    if credentials is None or credentials.invalid:
        print 'Run flow'
        credentials = tools.run_flow(auth_flow, storage)

    http = httplib2.Http()
    http = credentials.authorize(http)

    service = discovery.build('storage', 'v1', http=http)

    try:
        req = service.objects().list(bucket=BUCKET_NAME)
        resp = req.execute()
        print json.dumps(resp, indent=2)
    except client.AccessTokenRefreshError as e:
        print ('The credentials have been revoked or expired, please re-run')


if __name__ == '__main__':
    main()
