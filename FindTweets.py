
import tweepy
import json
import argparse

outputfile = "../TweetStream.json"

# This is the listener, resposible for receiving data
class TweetListener(tweepy.StreamListener):
    def on_data(self, data):
        # Twitter returns data in JSON format - we need to decode it first
        decoded = json.loads(data)
        try:
            with open(outputfile, 'a') as f:
                f.write(data)
                return True
        except (NameError, KeyError,AttributeError):
             pass

        return True
    def on_error(self, status):
        print status

        return True

if __name__ == '__main__':

    # parse arguments
    parser = argparse.ArgumentParser(description='Argument for Tweet Text')
    parser.add_argument('text', help="Tweet Text to Search")
    args = parser.parse_args()

    consumer_key = None
    consumer_secret = None
    access_token = None
    access_token_secret = None

    # check is function is missing
    if args.text is None:
        raise Exception("Required arguments: text")
    else:
        with open("../TweetAccess.cfg") as data_file:
            tweet_config = json.load(data_file)

        consumer_key = tweet_config["consumer_key"]
        consumer_secret = tweet_config["consumer_secret"]

        access_token = tweet_config["access_token"]
        access_token_secret = tweet_config["access_token_secret"]

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        tweet_listener = TweetListener()

        stream = tweepy.Stream(auth, tweet_listener)
        stream.filter(track=[args.text])