from tipfy import Rule, import_string


def get_rules(app):
    rules = []

    for app_module in app.get_config('tipfy', 'apps_installed'):
        try:
            # Load the urls module from the app and extend our rules.
            app_rules = import_string('%s.urls' % app_module)
            rules.extend(app_rules.get_rules(app))
        except ImportError:
            pass

    return rules
