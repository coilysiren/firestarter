# (( PROJECT CODENAME: FireStarter ))

Start a flask site really fast!

Like, super fast!!!

--- A [@lynncyrin](https://twitter.com/lynncyrin) project. [Source code here](https://github.com/LynnCo/firestarter) ---

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

At which point you should see (adjective)(noun).herokuapp.com pop up in your browser and display... this readme! Hopefully!!! Because if so that then that means you are now the proud owner of a website on the internet - even if that website is simply a guide on how to make this website ~

## Advanced tactics: Project Structure

    .venv/
    config/
    static/
    assets/
    scripts/
    templates/
    main.py
    Procfile
    readme.md
    requirements.txt
    .gitignore

Shown above is the top level view of the project. Some of these files and folders you should totally edit, others you should leave alone. I'll point a few out for you.

    config/
        config.yaml

Configurations go in here. Presently the only thing in here is config.yaml which contains sitewide variables. Please do edit this file! If you dont the internet will explode!

    paths/
        index.md
        404.md

[Markdown (.md)](http://daringfireball.net/projects/markdown/) and HTML (.html) files in the paths folder get turned into a URL for your wonderful website viewing audience. The URL does not contain the file extension. So putting a file called 'about.md' into the paths/ folder results in the contents of that file being displayed at your_website.com/about

404 and index are in here as examples!

    scripts/
        __init__.py
        cms.py

Scripts are python code! Python functionality can be placed inside of main.py but please do not do that. Instead put them in scripts/.

Presently the only script in this folder is cms.py, which handles turning markdon into HTML. __init__.py isn't actually a script, and instead is simply a [package marker](https://docs.python.org/2/tutorial/modules.html#packages)

    static/
        css/
            main.css
        js/
            main.js

Static files are viewable to the whole world, so do not put bank_account_info.txt in here. Presentially it contains main.css and main.js. main.js is empty because your friendly tutorial writer does not enjoy writing js. Then there is main.css which is compiled from main.scss (explained below). So there isn't really anything to do with the static/ folder.

    assets/
        main.scss

Assets contains things that build into static files. Presently the only thing in here is a single [Sass](http://sass-lang.com/) file but you can have as many as you want. [Coffeescript](http://coffeescript.org/) can go in here also, assuming you have a processor for it. Sass is great and you should learn it because it makes css TONS more reasonable.

    templates/
        analytics.html
        base.html
        head.html
        nav.html
        post.html

The templates folder contains templates (!), which are the building blocks of your website. Templates are a bit too complex for a quirky short description, so you should read about them on [Jinja's website](http://jinja.pocoo.org/docs/templates/). For the purpose of small projects, you can probably get away with not editing the templates much.

## Stretch Goals: What to do with your new website?

Here are some examples of things I am doing with a website framework such as this:

* Host a blog
* Perform gay twitter analytics
* Create a funding community
* Act as an organizing point for a QueerTrans collective
