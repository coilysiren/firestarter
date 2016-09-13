# (( PROJECT CODENAME: FireStarter ))

Start a flask site really fast!

Like, super fast!!!

--- A [Lynn Cyrin](http://lynncyrin.me) project. [Source code here](https://github.com/LynnCo/firestarter) ---

## Base Assumptions

This text assumes:

* basic familiarity with [python](https://www.python.org/) and html
* awareness of the uses of [git](http://git-scm.com/)
* the desire to make a website / web-app
* and **requires** you have installed:
    * [python](https://www.python.org/)
    * [git](http://git-scm.com/)
    * [pip](https://pip.pypa.io/en/latest/installing.html)
    * [virtualenv](https://virtualenv.pypa.io/en/latest/virtualenv.html) (which can be obtained via `$ pip install virtualenv`)

## Startup

First you obtain the code by running on command line

    $ git clone git@github.com:LynnCo/firestarter.git
    $ cd firestarter

Then install the packages that the project depeneds on. Right before you install the packages though, you should (but are not required to) initialize a virtualenv(ironment) and start it. Then you use pip to install all the project requirements.

    # pyenv on OSX
    $ echo "3.4" > .python-version

    $ virtualenv .venv --python=python3.4
    $ source .venv/bin/activate
    $ pip install -r requirements.txt

At which point, you can now run the website!

    $ python main.py

Then head your browser over to [http://localhost:5000](http://localhost:5000) to see... the same readme that you are currently reading! Except in website form!!!

Now if you want to turn this into something live on the internet that other people can see, I reccomend pushing the code to [heroku dot com](https://heroku.com). You would first need to create a (free) account and then give heroku your SSH key, a guide for which exists [here](https://devcenter.heroku.com/articles/keys).

    $ heroku login
    $ heroku create:app
    $ git push heroku
    $ heroku open

At which point you should see `(adjective)(noun).herokuapp.com` pop up in your browser and display... this readme! Hopefully!!! Because if so that then that means you are now the proud owner of a website on the internet - even if that website is simply a guide on how to make this website ~

## Advanced tactics: Project Structure

    templates/
    static/
    .venv/
    lib/
    requirements.txt
    runtime.txt
    config.yaml
    .gitignore
    readme.md
    Procfile
    main.py
    .env

Shown above is the top level view of the project. Some of these files and folders you'll be editing regularly, others you'll be leaving alone. I'll point a few out for you.

    config.yaml
    .env
    .gitignore

`config.yaml` holds basic site-wide configuration and data. So things like the website's name, URL, what port it runs on, etc. [Here](http://docs.ansible.com/ansible/YAMLSyntax.html) is a reference for yaml's syntax.

`.env` holds advanced, private configuration. Things like your database connection keys, account passwords. This information should **never** be public, or stored in git, which is why this file is paired with `.gitignore`. `.gitignore` makes it so that git will not track your file, resulting in you accidentally publishing your passwords on the internet. [python-dotenv](https://github.com/theskumar/python-dotenv) goes into a bit more detail about `.env` files.

Due to it being secret, the `.env` file won't exist when you copy the repo. You might also need to dig a little bit (eg. `show hidden files` or `ls -a`) to see it once it does exist.

    .venv
    requirements.txt

`.venv` holds the [virtual environment](http://docs.python-guide.org/en/latest/dev/virtualenvs/) for this project. It's a small python installation that lives inside your project folder.

`requirements.txt` is for telling pip what packages to install inside this virtual env(ironment).

    lib/
        __init__.py
        utils.py

The lib(rary) contains python code! Python functionality can be placed inside of main.py but please do not do that. Instead put it in `lib/`.

The main file in our library is `utils.py`. Arbitrary python code goes in here, such as a small function for loading files. `__init__.py` is [package marker](https://docs.python.org/2/tutorial/modules.html#packages) and not somewhere you should be putting code (unless you know what you are doing).

Scripts in the `lib` folder can be as small as two lines that print out *"Hello World"* and as large as a class that performs and graphs fourier transforms.

    static/
        scss/
        css/
        js/
        img/
        fonts/

Static files are viewable to the whole world, so do not put `txt/bank_account_info.txt` in here. Static folders can contain all sorts of things, but as a website builder you will mainly use them for css and javascript.

The `scss/` folder contains a [css preprocessor](http://sass-lang.com/), which I use because I tend to prefer it over directly writing css. The contents of the `scss/` folder are run through a converter and placed into `css/`. There are also css libraries such as [bootstrap](http://getbootstrap.com/) in the `css/` folder.

The `js/` folder mimics the `css/` folder ... or it would if your friendly tutorial writer did not have such an aversion to javascript.

`img/` and `fonts/` contain what you would expect.

    templates/
        partials/
            base.html
            head.html
            footer.html
        index.html

The templates folder contains templates (!), which are the building blocks of your website. The templating language is [jinja2](http://jinja.pocoo.org/docs/templates/), which builds into HTML.

In addition to jinja, the template files can contain [Markdown](http://daringfireball.net/projects/markdown/). `templates/index.html` shows an in use example of a template that renders markdown. This readme is also written in markdown!

The `templates/partials/` contains re-usable parts of your website - such as a navigation bar that would be present on every page.

The "base" templates directory (ie. where `templates/index.html`) lives is usually where I put "endpoint" templates. That is, the primary templates you point to in order to render a page, such as `about.html`, `contact.html`, etc.

    Procfile
    runtime.txt

The `Procfile` (which purposefully has no file extension) is used by [Heroku](https://devcenter.heroku.com/articles/procfile) to help run your website on a serious mode server. The commands in your `Procfile` are what Heroku will use to run your application, and generally `$ python main.py` is what you will be using.

`runtime.txt` tells Heroku what version of Python you will be using

    readme.md

You're reading it!

## Stretch Goals: What to do with your new website?

Here are some examples of things I am doing with a website framework such as this:

* Host a blog
* Perform gay twitter analytics
* Create a funding community
* Act as an organizing point for a QueerTrans collective
