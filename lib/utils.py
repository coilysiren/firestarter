# builtin
import os
import itertools
from os import environ as ENV
# external
import yaml
import dotenv
import flask_scss
import flask_cache
import flask_misaka


# private configs, from .env
dotenv.load_dotenv( dotenv.find_dotenv() )
# set base directory
base_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..')


def read_file(file_name):
    with open(file_name, 'r') as readme_file:
        content = readme_file.read()
    return content

def setup(app):
    # public configs, from config.yaml
    with open('config.yaml','r') as config_file:
        app.config.update( yaml.load( config_file ) )

    # extensions
    flask_misaka.Misaka(app)
    flask_scss.Scss(app, static_dir='static', asset_dir='static')
    cache = Cache(app, config={'CACHE_TYPE': 'simple'})

    return cache

def wait_for_tag_load(browser, element):
    counter = 0
    while not len(browser.find_by_tag(element)):
        counter += 1
        if counter >= 100: # 10 seconds
            raise Exception('timeout while waiting for \"{}\"'.format(element))
        else:
            time.sleep(0.1)

def login_and_get_table():
    with splinter.Browser('phantomjs') as browser:
        try:
            # login
            browser.driver.set_window_size(1366,768)
            browser.visit('https://iwantclips.com/login/fancy_login')
            wait_for_tag_load(browser, 'form')
            browser.fill('email', ENV['IWC_USER'])
            browser.fill('password', ENV['IWC_PASS'])
            browser.find_by_name('submit').click()
            # get the content table
            browser.visit('https://iwantclips.com/model/content_store')
            wait_for_tag_load(browser, 'tbody')
            content = browser.find_by_tag('tbody')[0].html
            print(content)
            return content
        except Exception as e:
            browser.driver.save_screenshot('error.png')
            raise

def table_html_to_dict(table_str):
    soup = bs4.BeautifulSoup(table_str, 'html.parser')
    table_dict = {}
    for video in soup.find_all('tr'):
        columns = video.find_all('td')
        name    = columns[4].find('a').contents[0]
        link    = columns[4].find('a').get('href')
        date    = columns[3].contents[0]
        price   = columns[5].contents[0]
        sales   = columns[6].contents[0]
        table_dict[name] = {
            'date': date,
            'price': price,
            'sales': sales,
            'link': link
        }
    return table_dict

def merge_table_with_local_data(path, table):
    path = os.path.join(base_dir, 'data/shoot_percents.yaml')
    with open(path, 'r') as yaml_file:
        shoot_data = yaml.load(yaml_file)
    for video in table.keys():
        table[video]['Roles'] = shoot_data[video]['Roles']
        table[video]['Workers'] = shoot_data[video]['Workers']
    return table

def get_scaling_factor(table):
    for video in table.keys():
        total_percent = 0
        total_percent += int(table[video]['Roles']['QAPC'].strip('%'))

        role_tally = list(itertools.chain.from_iterable(
            table[video]['Workers'].values()
        ))

        for role in role_tally:
            total_percent += int(table[video]['Roles'][role].strip('%'))

        scaling_factor = 100 / total_percent
        table[video]['scaling factor'] = scaling_factor
    return table

def get_worker_percents(table):
    for video in table.keys():
        table[video]['percents'] = {}
        for worker, roles in table[video]['Workers'].items():
            percent = 0
            for role in roles:
                unscaled_percent = int(table[video]['Roles'][role].strip('%'))
                percent += unscaled_percent * table[video]['scaling factor']
            table[video]['percents'][worker] = percent
        unscaled_percent = int(table[video]['Roles']['QAPC'].strip('%'))
        table[video]['percents']['QAPC'] = unscaled_percent * table[video]['scaling factor']
    return table

def get_total_earnings(table):
    for video in table.keys():
        price = float(table[video]['price'].strip('$'))
        sales = int(table[video]['sales'])
        IWC_payout = float(0.7)
        table[video]['total earnings'] = price * sales * IWC_payout
    return table

def get_worker_earnings(table):
    for video in table.keys():
        table[video]['earnings'] = {}
        for worker, percent in table[video]['percents'].items():
            earnings = table[video]['total earnings'] * percent / 100
            table[video]['earnings'][worker] = earnings
    return table

def populate_shoot_table():
    table = login_and_get_table()

    table = table_html_to_dict(table)
    table = merge_table_with_local_data(table)
    table = get_scaling_factor(table)
    table = get_worker_percents(table)
    table = get_total_earnings(table)
    table = get_worker_earnings(table)

    return table
