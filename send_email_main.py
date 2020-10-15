
from __future__ import print_function
import httplib2
import os


from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_known_args()
except ImportError:
    flags = None

import auth


"""def get_labels():
    results = service.users().labels().list(userId='me').execute()
    labels = results.get('labels', [])

    if not labels:
        print('No labels found.')
    else:
        print('Labels:')
        for label in labels:
            print(label['name'])"""

SCOPES = 'https://mail.google.com/'
CLIENT_SECRET_FILE = 'json/credentials.json'
APPLICATION_NAME = 'Automatic TOll Collector - Email'
authInst = auth.auth(SCOPES,CLIENT_SECRET_FILE,APPLICATION_NAME)
credentials = authInst.get_credentials()

http = credentials.authorize(httplib2.Http())
service = discovery.build('gmail', 'v1', http=http)

import send_email

def send_email_from_backend_with_attachment(message_content, image_path):

	sendInst = send_email.send_email(service)
	message = sendInst.create_message_with_attachment('addyouremail@gmail.com','addyouremail@gmail.com','New Delhi Toll Bill',message_content, image_path )
	sendInst.send_message('me',message)
