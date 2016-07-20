from datetime import datetime

from flask import render_template

from app import *

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', utc_time=datetime.utcnow(), time=datetime.now())


@app.errorhandler(404)
def not_found(e):
    return { 
        'code': 404, 
        'msg': "Not found" 
        }, 404 