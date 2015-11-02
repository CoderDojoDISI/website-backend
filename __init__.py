import os
from eve import Eve
from eve.auth import BasicAuth

from .generateID import generateID
import api.settings

class MyAuth(BasicAuth):
    def check_auth(self, username, password, allowed_roles, resource, method):
        return True


SETTINGS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'settings.py')

app = Eve(auth=MyAuth, settings=SETTINGS_PATH)

app.on_insert += generateID