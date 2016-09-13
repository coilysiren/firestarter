# internal
from os import environ as ENV
# external
import yaml
import dotenv
import flask_misaka
import flask_scss
import twython
from twython import Twython

def read_file(file_name):
    with open(file_name, 'r') as readme_file:
        content = readme_file.read()
    return content

def setup(app):
    # public configs, from config.yaml
    with open('config.yaml','r') as config_file:
        app.config.update( yaml.load( config_file ) )

    # private configs, from .env
    dotenv.load_dotenv( dotenv.find_dotenv() )

    # extensions
    flask_misaka.Misaka(app)
    flask_scss.Scss(app, static_dir='static', asset_dir='static')

    # twitter api
    app.twitter = twython.Twython(
        ENV["consumer_key"],
        ENV["consumer_secret"],
        ENV["access_token"],
        ENV["access_token_secret"]
    )

def twitter_url_to_int(url):
    return int(url.split('/')[-1])

def twitter_id_to_hashtags(tweet_id):
    from main import app
    tweet = app.twitter.show_status(id=tweet_id)
    hashtags = []
    for entity in tweet['entities']['hashtags']:
        hashtags.append(entity['text'])
    return hashtags
