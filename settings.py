import os

from api.resources.courses import courses
from api.resources.events import events
from api.resources.faq import faq
from api.resources.mentors import mentors
from api.resources.tutorials import tutorials

MONGO_HOST = os.environ["MONGO_HOST"]
MONGO_USERNAME = os.environ["MONGO_USERNAME"]
MONGO_PASSWORD = os.environ["MONGO_PASSWORD"]
MONGO_DBNAME = os.environ["MONGO_DBNAME"]

RESOURCE_METHODS = ['GET', 'POST']
ITEM_METHODS = ['GET', 'PATCH']

PUBLIC_METHODS = ['GET']
PUBLIC_ITEM_METHODS = ['GET']

URL_PREFIX = "api"
XML = False
EXTENDED_MEDIA_INFO = ['content_type']

DOMAIN = {
    'faq': faq,
    'events': events,
    'mentors': mentors,
    'courses' : courses,
    'tutorials': tutorials
}

if os.environ["DEVELOPMENT"] :
    DEBUG = True
