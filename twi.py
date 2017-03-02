#importing necessary packages
from twitter import Twitter,OAuth
import configparser
import sys

#function to read the "config.ini" file, which stores the Twitter API access credentials
#arguments:NONE
#returns: dict "tokens" if successfully read config.ini,else None
def readConfig():
    try:
        cp = configparser.ConfigParser()
        cp.read("config.ini")
        tokens = cp["access_tokens"]
        return tokens
    except:
        return None

#fetchTweets uses the the Twitter,OAuth module from twitter package to fetch the tweets
#arguments: hashtag:the name of tag,count: the minimum number of retweets
#returns: Nothing
def fetchTweets(hashtag,count):
    tokens = readConfig()
    if tokens is None:
        print "Error in importing the config.ini"
        sys.exit()
    oauth_token = tokens["oauth_token"]
    oauth_token_secret = tokens["oauth_token_secret"]
    CONSUMER_KEY = tokens["consumer_key"]
    CONSUMER_SECRET = tokens["consumer_secret"]
    try:
        t = Twitter(auth=OAuth(oauth_token,oauth_token_secret,CONSUMER_KEY,CONSUMER_SECRET))
        Tweets = t.search.tweets(q = hashtag)
        if len(Tweets["statuses"]) == 0:
            print "No Tweets for this hashtag"
        for item in Tweets["statuses"]:
            if item["retweet_count"] >= count:
                print item["text"]
    except:
        print "FetchData() Operation didn't succeed."
        sys.exit()

def main():
    try:
        hashtag = "#"+str(sys.argv[1])
        count = int(sys.argv[2])
        if count < 0:
            print "Retweet counts cannot be negative."
            sys.exit()
    except IndexError:
        print "Syntax: python twi.py <hashtag> <retweet_count>"
        print "Example: python twi.py custserv 1"
        sys.exit()
    fetchTweets(hashtag,count)

if __name__ == '__main__':
    main()
