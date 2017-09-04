import argparse
import ConfigParser
import io
import json
import os
import datetime
from twitter import Twitter, OAuth

# OAuth
with open("config.ini") as f:
	twitter_config = f.read()
config = ConfigParser.RawConfigParser(allow_no_value=True)
config.readfp(io.ByteIO(twitter_config))
CONSUMER_KEY = config.get('twitter', 'CONSUMER_KEY')
CONSUMER_SECRET = config.get('twitter', 'CONSUMER_SECRET')
ACCESS_TOKEN = config.get('twitter', 'ACCESS_TOKEN')
ACCESS_SECRET = config.get('twitter', 'ACCESS_SECRET')
oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
twitter_searchApi= Twitter(auth=oauth)

# argparse
parser = argparse.ArgumentParser(description='search tweets regarding certain term in certain created date')
parser.add_argument("--search_term", help="search term")
parser.add_argument("--tweet_date", help="tweet created date in yyyy-mm-dd")
args = parser.parse_args()
search_term = args.search_term
tweet_date_str = args.tweet_date
tweet_date = datetime.datetime.strptime(tweet_date_str, '%Y-%m-%d').date()
until_date = tweet_date + datetime.timedelta(days =1 )
until_date_str = until_date.strftime("%Y-%m-%d")
today_str = datetime.datetime.now().strftime("%Y-%m-%d")
today = datetime.datetime.today().date()
today_back_oneWeek = today - datetime.timedelta(days = 8)
today_back_oneWeek_str = today_back_oneWeek.strftime("%Y-%m-%d")

# functions
def createFolder(folderName):
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    dateTime = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    path = folderName + '/' + tweet_date_str
    isExists=os.path.exists(path)
    if(not isExists):
        os.makedirs(path)
    return path + '/'  + dateTime

# fetch data 
result = twitter_searchApi.geo.search(query="USA", granularity="country")
place_id = result['result']['places'][0]['id']
iterator = twitter_searchApi.search.tweets(q = search_term + '&place:'+place_id, since = tweet_date_str, until = until_date_str, lang = 'en',count=100)
test = twitter_searchApi.search.tweets(q='#nlproc&place:'+place_id, result_type='recent', lang='en', count=100)
path = createFolder(search_term)
with open(path + '.json', 'w') as f:
    f.write(json.dumps(iterator, indent = 4))