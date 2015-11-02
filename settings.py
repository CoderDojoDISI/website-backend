import os
from api.resources import faq

MONGO_USERNAME = os.environ["MONGO_USERNAME"]
MONGO_PASSWORD = os.environ["MONGO_PASSWORD"]
MONGO_DBNAME = os.environ["MONGO_DBNAME"]

RESOURCE_METHODS = ['GET', 'POST']
ITEM_METHODS = ['GET']
URL_PREFIX = "api"
XML = False


DOMAIN = {
    'faq': faq.faq
}

if os.environ["DEVELOPMENT"] :
    DEBUG = True
