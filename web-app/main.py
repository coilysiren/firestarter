'''
__name__ = blog.py
__desc__ = Routing and content generation file
__sign__ = Lynn Cyrin

Use:
[Production] '$ foreman start'
[Developement] '$ python blog.py' (runs in debug mode)
'''


#builtin scripts
import glob
#external scripts
import yaml
import flask
import flask.ext.scss


#start app and set configuration


app = flask.Flask(__name__, static_folder='static', static_url_path='')
app.config.from_object(__name__)
for key, value in yaml.load(file('../config/config.yaml','r')).items():
    app.config[key] = value


#views


#index page
@app.route('/index')
@app.route('/')
def index ():
    return flask.render_template('post.html',
        page_title=app.config['SITENAME'],
        page_desc=app.config['DESC'],
        post_urls=['',])
@app.route('/static/<path:filename>')
def base_static(filename):
    return flask.send_from_directory(app.root_path + '/static/', filename)

@app.errorhandler(404)
def page_not_found (e):
    return flask.render_template('post.html',
        page_title=app.config['SITENAME']+' // Error 404',
        page_desc='Page Not Found',
        post_urls=['pages/404.html'])


#debug mode start options


if __name__ == '__main__':
    app.config['DEBUG'] = True
    flask.ext.scss.Scss(app)
    app.run()
