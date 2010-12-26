from tipfy import Rule


def get_rules(app):
    rules = [
        Rule('/', handler='apps.foursquare_connect.handlers.LoginHandler'),
    ]

    return rules
