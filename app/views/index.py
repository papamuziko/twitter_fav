from datetime import datetime

from flask import Flask
from flask import render_template, redirect
from flask import g, session, request, url_for, flash
from flask_oauthlib.client import OAuth

from config import *
from app import *

oauth = OAuth()
twitter = oauth.remote_app('twitter',
    base_url='https://api.twitter.com/1.1/',
    request_token_url='https://api.twitter.com/oauth/request_token',
    access_token_url='https://api.twitter.com/oauth/access_token',
    authorize_url='https://api.twitter.com/oauth/authenticate',
    consumer_key=CONFIG['twitter']['customer_key'],
    consumer_secret=CONFIG['twitter']['customer_secret']
)

@app.route('/', methods=['GET'])
def index():
    username = None
    if g.user is not None:
        resp = twitter.request('account/verify_credentials.json')
        username = resp.data['screen_name']
            
    return render_template('index.html', utc_time=datetime.utcnow(), time=datetime.now(), username=username)


@app.route('/search', methods=['POST'])
def search():
    q = request.form.get('q')
    return q

@twitter.tokengetter
def get_twitter_token():
    if 'twitter_oauth' in session:
        resp = session['twitter_oauth']
        return resp['oauth_token'], resp['oauth_token_secret']


@app.before_request
def before_request():
    g.user = None
    if 'twitter_oauth' in session:
        g.user = session['twitter_oauth']


@app.route('/login')
def login():
    callback_url = url_for('oauthorized', next=request.args.get('next'))
    return twitter.authorize(callback=callback_url or request.referrer or None)


@app.route('/logout')
def logout():
    session.pop('twitter_oauth', None)
    return redirect(url_for('index'))


@app.route('/oauthorized')
def oauthorized():
    resp = twitter.authorized_response()
    if resp is None:
        flash('You denied the request to sign in.')
    else:
        session['twitter_oauth'] = resp
    return redirect(url_for('index'))    



@app.errorhandler(404)
def not_found(e):
    return { 
        'code': 404, 
        'msg': "Not found" 
        }, 404 