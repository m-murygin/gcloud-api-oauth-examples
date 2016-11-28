#!/usr/bin/python

import httplib2
import json
import os
import webbrowser

from apiclient import discovery
from oauth2client import client

SECRET_NAME = 'client_secret.json'
client_secret = os.path.join(os.getcwd(), SECRET_NAME)


def main():
    flow = client.flow_from_clientsecrets(
        client_secret,
        scope='https://www.googleapis.com/auth/devstorage.read_only',
        redirect_uri='urn:ietf:wg:oauth:2.0:oob')

    auth_uri = flow.step1_get_authorize_url()
    webbrowser.open(auth_uri)

    auth_code = raw_input('Enter the auth code: ')

    credentials = flow.step2_exchange(auth_code)
    http_auth = credentials.authorize(httplib2.Http())

    storageService = discovery.build('storage', 'v1', http=http_auth)

    req = storageService.buckets().list(project="mm-development-2")
    print json.dumps(req.execute(), indent=2)


if __name__ == '__main__':
    main()
