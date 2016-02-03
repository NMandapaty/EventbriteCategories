import json

TOKEN = 'BKKRDKVUVRC5WG4HAVLT'
CATEGORIES_URL = 'https://www.eventbriteapi.com/v3/categories/'
SEARCH_URL = 'https://www.eventbriteapi.com/v3/events/search/'

"""
None of the models need to be stored in a database, so none of them
subclass models.Model.

These classes simply exist to easily extract the necessary information 
from the given JSON objects.
"""

class Category():
    def __init__(self, catObject):
        self.id = catObject['id']
        self.name = catObject['name']
        self.shortname = catObject['short_name']

    def __str__(self):
        return self.name

class Event():
    def __init__(self, eventObject):
        e = eventObject
        self.id = e['id']
        self.name = e['name']['text']
        self.description = e['description']['html']
        self.url = e['url']
        #some events do not have logos
        logo = e.get('logo', None)
        if logo:
            self.logo = logo['url']
        self.start_time = e['start']
        self.end_time = e['end']

    def __str__(self):
        return self.name
