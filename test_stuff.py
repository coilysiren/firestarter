from lib import utils

def test_should_get_a_url_and_turn_it_into_an_integer():
    twitter_url = "https://twitter.com/lynncyrin/status/775822710140203008"
    expected_twitter_id = 775822710140203008
    twitter_id = utils.twitter_url_to_int(twitter_url)
    assert twitter_id == expected_twitter_id
