import os

DEV_CONFIG = {
    'debug': True,
    'env': 'development',
    'host': '0.0.0.0',
    'port': 3333,
    'twitter': {
        'customer_key': os.environ.get('TW_CUSTOMER_KEY'),
        'customer_secret': os.environ.get('TW_CUSTOMER_SECRET'),
        'callback_url': "http://0.0.0.0:3333/oauthorized"
    },
    'secret_key': os.environ.get('TWITTER_FAV_SECRET')
}

PROD_CONFIG = {
    'debug': False,
    'env': 'production',
    'host': '0.0.0.0',
    'port': 3333,
    'twitter': {
        'customer_key': os.environ.get('TW_CUSTOMER_KEY'),
        'customer_secret': os.environ.get('TW_CUSTOMER_SECRET'),
        'callback_url': "http://twitter-gui.hbtn.io/oauthorized"        
    },
    'secret_key': os.environ.get('TWITTER_FAV_SECRET')
}

CONFIG = DEV_CONFIG
if os.environ.get('ENV') == 'production':
    CONFIG = PROD_CONFIG
