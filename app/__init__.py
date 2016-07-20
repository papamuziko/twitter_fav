from flask import Flask
from flask_cors import CORS

from config import *

app = Flask(__name__)
app.secret_key = CONFIG['secret_key']
cors = CORS(app, resources={r"/*": {"origins": "*"}})

from views import * 
