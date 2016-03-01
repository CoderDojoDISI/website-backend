from eve import Eve
from eve.auth import BasicAuth
from flask import Response, abort, request

import settings
from generateID import generateID


class MyAuth(BasicAuth):
    def check_auth(self, username, password, allowed_roles, resource, method):
        if username == "admin" & password == "admin":
            return True
        else:
            return False

    def authenticate(self):
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            resp = Response(None, 401, {'WWW-Authenticate': 'xBasic'})
            abort(401, description='Please provide proper credentials', response=resp)
        else:
            resp = Response(None, 401, {'WWW-Authenticate': 'Basic'})
            abort(401, description='Please provide proper credentials', response=resp)


SETTINGS_PATH = settings.__file__

app = Eve(auth=MyAuth, settings=SETTINGS_PATH)

app.on_insert += generateID

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8001, debug=True)
