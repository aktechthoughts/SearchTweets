import tweepy
import json
import csv
import urllib

outputfile = "../TweetStream.json"

# This is the listener, resposible for receiving data
class TweetListener(tweepy.StreamListener):
    def on_data(self, data):
        # Twitter returns data in JSON format - we need to decode it first
        decoded = json.loads(data)
        try:

        except (NameError, KeyError,AttributeError):
             pass

        return True
    def on_error(self, status):
        print status

        return True

if __name__ == '__main__':
    tweet_listener = TweetListener()
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = tweepy.Stream(auth, tweet_listener)
    stream.filter(track=[accountvar])


