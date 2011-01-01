config = {}

config['tipfy'] = {
    # Enable debugger. It will be loaded only in development.
    'middleware': [
        'tipfy.ext.debugger.DebuggerMiddleware',
    ],

    'apps_installed': [
        'apps.foursquare_connect',
    ],
}

config['tipfy.ext.session'] = {
    'secret_key': 'my_strong_secret_key',
    'default_backend': 'memcache'
}
