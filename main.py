# builtin
import glob
# external
import yaml
import flask
import flask_scss
import flask_misaka


# start app and set configuration
app = flask.Flask(__name__, static_folder='static', static_url_path='/static', )
app.config.from_object(__name__)
with open('config.yaml','r') as config_file:
    for key, value in yaml.load(config_file).items():
        app.config[key] = value


# Views! i.e. what the user gets when they type in our url

# this renders the readme as the index page...
@app.route('/')
def index ():
    with open('readme.md', 'r') as readme_file:
        content = readme_file.read()
    return flask.render_template('partials/base.html', content=content)

# ...but this is the index page view you probably want
# @app.route('/')
# def index ():
#     return flask.render_template('index.html')


if __name__ == '__main__':
    flask_scss.Scss(app, static_dir='static', asset_dir='static')
    flask_misaka.Misaka(app)
    app.run(port = app.config.get("PORT", 5000))
