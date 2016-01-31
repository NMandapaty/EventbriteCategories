import json

# Create your models here.
TOKEN = 'BKKRDKVUVRC5WG4HAVLT'
CATEGORIES_URL = 'https://www.eventbriteapi.com/v3/categories/'
SEARCH_URL = 'https://www.eventbriteapi.com/v3/events/search/'

#None of the models need to be stored in a database, so none of them
#subclass models.Model

'''
Category represents one Eventbrite event category
'''
class Category():
    def __init__(self, catObject):
        self.id = catObject['id']
        self.name = catObject['name']
        self.shortname = catObject['short_name']

    def toJSON(self):
        obj = {
            'id': self.id,
            'name': self.name,
            'shortname': self.shortname
        }
        return json.dumps(obj)

    def __str__(self):
        return self.name

class Event():
    def __init__(self, eventObject):
        e = eventObject
        self.id = e['id']
        self.name = e['name']['html']
        self.description = e['description']['html']
        self.url = e['url']
        self.vanity_url = e['vanity_url']
        self.logo = e['logo']
        self.start_time = e['start']
        self.end_time = e['end']

    def toJSON(self):
        obj = {
            'id': self.id,
            'name': self.name,
            'description': self.descirption,
            'url': self.url,
            'vanity_url': self.vanity_url,
            'logo': self.logo,
            'start_time': self.start_time,
            'end_time': self.end_time
        }
        return json.dumps(obj)

    def __str__(self):
        return self.name
