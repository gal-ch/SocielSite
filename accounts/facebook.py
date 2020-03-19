from __future__ import unicode_literals, absolute_import
import re

import facebook
from django.contrib.gis import db

from facebook import GraphAPI
import facebook

import requests




class Facebook():
    graph = None


    def __init__(self, token):
        self.graph = facebook.GraphAPI(access_token=token, version='2.12')

    def get_id(self):
        event = self.graph.get_object(id='me')
        return event['id']

    def get_profile(self, username):
        event = self.graph.get_object(id='me', fields='id,first_name,last_name,email,picture.type(large)')
        obj = {
            "username": re.sub(r'\s+', '', username),
            "email": event['email'] if 'email' in event else event['id'],
            "first_name": event['first_name'],
            "last_name": event['last_name'],
            "idsn": event['id'],
        }
        return obj

    def get_friends(self):
        event = self.graph.get_all_connections(id='me', connection_name='friends')
        return [x['id'] for x in event]
