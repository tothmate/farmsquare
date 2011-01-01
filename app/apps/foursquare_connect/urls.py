from tipfy import Rule


def get_rules(app):
    rules = [
        Rule('/foursquare-login', handler='apps.foursquare_connect.handlers.LoginHandler'),
        Rule('/foursquare-login-success', handler='apps.foursquare_connect.handlers.LoginSuccessHandler'),
    ]

    return rules
