from tipfy import RequestHandler
from tipfy.ext.jinja2 import render_response
from tipfy.ext.session import SessionMiddleware, SessionMixin

import foursquare


class VenueListHandler(RequestHandler, SessionMixin):
    middleware = [SessionMiddleware]

    def get(self):
        # TODO: move it to a decorator
        if self.session["fs"] is None:
            return self.redirect("/foursquare-login")
        fs = self.session["fs"]
        
        # NOTE: Do we always have the right fs in session?
        history = foursquare.all_history(fs)
        venues = {}
        for checkin in history:
            if checkin["venue"]["id"] in venues:
                continue
            venues[checkin["venue"]["id"]] = {
                "name": checkin["venue"]["name"]
            }
        
        return render_response("venue_list.html", venues=venues)


class LoginHandler(RequestHandler, SessionMixin):
    middleware = [SessionMiddleware]

    def get(self):
        # TODO: move it to config
        credentials = foursquare.OAuthCredentials("I2Z50NWD45L0XCZNARRS3A15TTKCKSI0WWR2A3HCYHZDIE44", "Z2PBQ40CDNBVRNNSM4JK5ZVPK0IWWEVJKTBMWOGM3PIXOA4Y")
        fs = foursquare.Foursquare(credentials)
        # TODO: don't hardcode server
        app_token = fs.request_token(oauth_callback="http://localhost:8080/foursquare-login-success-callback")
        auth_url = fs.authorize(app_token)
        self.session["fs"] = fs
        self.session["app_token"] = app_token
        return render_response("foursquare_login.html", message=auth_url)


class LoginSuccessCallbackHandler(RequestHandler, SessionMixin):
    middleware = [SessionMiddleware]

    def get(self):
        # TODO: deny handler
        
        # TODO: error handling
        oauth_verifier = self.request.args.get("oauth_verifier")
        # NOTE: Avoid storing it in session?
        fs = self.session["fs"]
        app_token = self.session["app_token"]
        
        user_token = fs.access_token(app_token, oauth_verifier)
        fs.credentials.set_access_token(user_token)
        del self.session["app_token"]
        
        return self.redirect("/")
