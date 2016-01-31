import requests
from categories.models import Category, Event

TOKEN = 'BKKRDKVUVRC5WG4HAVLT'
CATEGORIES_URL = 'https://www.eventbriteapi.com/v3/categories/'
SEARCH_URL = 'https://www.eventbriteapi.com/v3/events/search/'

'''
Returns a list of category objects
'''
def get_categories():
    r = requests.get(CATEGORIES_URL, params={'token': TOKEN}).json()
    categories = [Category(cat) for cat in r['categories']]

    return categories

'''
Returns a list of event objects for the given page, as well as the total number
of pages
'''
def get_events(page=1, *categories):
    params = {
        'token': TOKEN,
        'categories': ','.join(categories),
        'page': page
    }
    r = requests.get(SEARCH_URL, params=params).json()

    page_count = r['pagination']['page_count']

    #only keep relevant fields
    events = [Event(e) for e in r['events']]
    return {
        'events': events,
        'page_count': page_count
    }
