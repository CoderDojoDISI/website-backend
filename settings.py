import os

import resources as res

MONGO_HOST = os.environ["MONGO_HOST"]
MONGO_USERNAME = os.environ["MONGO_USERNAME"]
MONGO_PASSWORD = os.environ["MONGO_PASSWORD"]
MONGO_DBNAME = os.environ["MONGO_DBNAME"]

RESOURCE_METHODS = ['GET', 'POST']
ITEM_METHODS = ['GET', 'PATCH']

if os.environ.get("DEVELOPMENT") == 'true':
  PUBLIC_METHODS = ['GET','POST']
  PUBLIC_ITEM_METHODS = ['GET','PATCH','PUT','DELETE']
else:

  PUBLIC_METHODS = ['GET']
  PUBLIC_ITEM_METHODS = ['GET']

URL_PREFIX = "api"
XML = False
EXTENDED_MEDIA_INFO = ['content_type']

DOMAIN = {
    'faq': res.faq,
    'events': res.events,
    'mentors': res.mentors,
    'courses': res.courses,
    'tutorials': res.tutorials
}

STANDARD_ERRORS = [400, 401, 403, 404, 405, 406, 410, 412, 422, 428]

if os.environ.get("DEVELOPMENT") == 'true':
    DEBUG = True
