from __future__ import print_function
import httplib2
import os
from django.contrib import messages
from django.shortcuts import render

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
from .models import Client, Pregnancy

import datetime

try:
    import argparse

    flags = tools.argparser.parse_args([])
except ImportError:
    flags = None

SCOPES = 'https://www.googleapis.com/auth/calendar'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'pm-planner'

def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'calendar-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials


def create_calendar_entries(entries):
    responses = []
    for entry in entries:
        responses.append(create_calendar_entry(entry))
    return responses


def create_calendar_entry(entry):
        credentials = get_credentials()
        http = credentials.authorize(httplib2.Http())
        service = discovery.build('calendar', 'v3', http=http)
        event = {
            'summary': entry['name'],
            'location': entry['address'],
            'description': entry['notes'],
            'start': {
                'date': entry['due_date'],
            },
            'end': {
                'date': entry['due_date'],
            },

            'reminders': {
                'useDefault': False,
                'overrides': [
                    {'method': 'email', 'minutes': 24 * 60},
                    {'method': 'popup', 'minutes': 10},
                ],
            },
            'visibility': 'private',
            'anyoneCanAddSelf': False,
        }
        event = service.events().insert(calendarId='primary', body=event).execute()
        event_url = event.get('htmlLink')
        event_summary = event.get('summary')
        response = {"url": event_url, "name": event_summary}

        return response
