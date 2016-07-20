from config import *
from app import app 

if __name__ == '__main__':
    app.config['JSON_ADD_STATUS'] = False
    app.config['JSON_DATETIME_FORMAT'] = '%d/%m/%Y %H:%M:%S'

    app.run(host=CONFIG['host'], port=CONFIG['port'], debug=CONFIG['debug'])  