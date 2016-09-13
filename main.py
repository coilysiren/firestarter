'''
__name__ = main.py
__desc__ = Routing and content generation file
__sign__ = Lynn Cyrin

Use:
[Production] '$ foreman start'
[Developement] '$ python main.py' (runs in debug mode)
'''

# builtin
import glob
# external
import yaml
import flask
import flask_scss
import flask_misaka
# custom
from scripts import cms

# shortcuts
build = cms.build_html

# start app and set configuration
app = flask.Flask(__name__, static_folder='static', static_url_path='')
app.config.from_object(__name__)
with open('config/config.yaml','r') as config_file:
    for key, value in yaml.load(config_file).items():
        app.config[key] = value

# Views! i.e. what the user gets when they type in our url

# the index page is special because its path is empty.
#
# The first thing you will want to do is change this
#     return flask.render_template('post.html', html_content=build("readme"))
# to this
#     return flask.render_template('post.html', html_content=build("paths/index"))
#
@app.route('/')
def index ():
    return flask.render_template('post.html', html_content=build("readme"))

# every other path reads from paths/<url_input>
# ex: website.com/cats -> firestarter/paths/cats
@app.route('/<path>')
def dynamic_path(path):
    # first check that path is empty, if so then 404
    if len(glob.glob('paths/'+path+'*')) == 0: return page_not_found(404)
    return flask.render_template('post.html', html_content=build("paths/"+path))

if __name__ == '__main__':
    flask_scss.Scss(app)
    flask_misaka.Misaka(app)
    app.run(port = app.config.get("PORT", 5000))
