import requests
from categories.models import Category, Event

TOKEN = 'BKKRDKVUVRC5WG4HAVLT'
CATEGORIES_URL = 'https://www.eventbriteapi.com/v3/categories/'
SEARCH_URL = 'https://www.eventbriteapi.com/v3/events/search/'

def get_categories():
    """
    Returns a list of category objects
    """

    r = requests.get(CATEGORIES_URL, params={'token': TOKEN})
    if r.status_code == 429: #hit rate limit
        return None, "Hit the Eventbrite API rate limit. Try again in a bit."

    categories = [Category(cat) for cat in r.json()['categories']]
    return (categories, '')

def get_events(categories, page=1):
    """
    Returns a list of event objects for the given page, as well as the total number
    of pages
    """

    params = {
        'token': TOKEN,
        'categories': ','.join(categories),
        'page': page
    }
    r = requests.get(SEARCH_URL, params=params)
    if r.status_code == 429: #hit rate limit
        return None, None, "Hit the Eventbrite API rate limit. Try again in a bit."

    page_count = r.json()['pagination']['page_count']

    events = [Event(e) for e in r['events']]
    return (events, page_count, '')
