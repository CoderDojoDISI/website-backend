import os
from eve import Eve
from eve.auth import BasicAuth
from flask import Response, abort, request

from .generateID import generateID
import api.settings

class MyAuth(BasicAuth):
    def check_auth(self, username, password, allowed_roles, resource, method):
        return False
    def authenticate(self):
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest' :
            resp = Response(None, 401, {'WWW-Authenticate': 'xBasic'})
            abort(401, description='Please provide proper credentials',response=resp)
        else:
            resp = Response(None, 401, {'WWW-Authenticate': 'Basic'})
            abort(401, description='Please provide proper credentials',response=resp)


SETTINGS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'settings.py')

app = Eve(auth=MyAuth, settings=SETTINGS_PATH)

app.on_insert += generateID