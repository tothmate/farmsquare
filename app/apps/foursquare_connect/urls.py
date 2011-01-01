from tipfy import Rule


def get_rules(app):
    rules = [
        Rule('/', handler='apps.foursquare_connect.handlers.VenueListHandler'),
        Rule('/foursquare-login', handler='apps.foursquare_connect.handlers.LoginHandler'),
        Rule('/foursquare-login-success-callback', handler='apps.foursquare_connect.handlers.LoginSuccessCallbackHandler'),
    ]

    return rules
