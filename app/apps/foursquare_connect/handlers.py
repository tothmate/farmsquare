from tipfy import RequestHandler
from tipfy.ext.jinja2 import render_response


class LoginHandler(RequestHandler):
    def get(self):
        return render_response('foursquare_login.html', message='capp')
