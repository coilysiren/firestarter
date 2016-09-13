from lib import utils

def test_should_get_a_url_and_turn_it_into_an_integer():
    twitter_url = "https://twitter.com/lynncyrin/status/775822710140203008"
    expected_twitter_id = 775822710140203008
    twitter_id = utils.twitter_url_to_int(twitter_url)
    assert twitter_id == expected_twitter_id

def test_should_turn_twitter_id_into_list_of_hashtags():
    twitter_id = 775824326411026433
    expected_hashtags = ['twitter', 'tweet']
    hashtags = utils.twitter_id_to_hashtags(twitter_id)
    assert hashtags == expected_hashtags
