# external
import yaml
import dotenv
import flask_misaka
import flask_scss


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
