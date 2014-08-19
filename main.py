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
import flask.ext.scss
# custom
from scripts import scripts

# shortcuts
render = flask.render_template
build = scripts.build_html

# start app and set configuration
app = flask.Flask(__name__, static_folder='static', static_url_path='')
app.config.from_object(__name__)
for key, value in yaml.load(file('config/config.yaml','r')).items():
    app.config[key] = value

# Views! i.e. what the user gets when they type in our url

# index is special because its path can be blank
@app.route('/')
def index ():
    return render('post.html', html_content=build("index"))

# 404 is special because it needs @app.errorhandler(404)
@app.errorhandler(404)
def page_not_found (e):
    return render('post.html', html_content=build("404"))

# every other path does markdown -> html
@app.route('/<path>')
def dynamic_path(path):
    # check if path exists, if not 404
    if len(glob.glob('paths/'+path+'*')) == 0: return page_not_found(404)
    # otherwise, build it!
    return render('post.html', html_content=build(path))

# except for /static/* in which case we render the file itself
@app.route('/static/<path:filename>')
def base_static(filename):
    return flask.send_from_directory(app.root_path + '/static/', filename)

# debug mode start options

if __name__ == '__main__':
    app.config['DEBUG'] = True
    flask.ext.scss.Scss(app)
    app.run()
