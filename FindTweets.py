#!/usr/bin/python

################################################################################
import argparse
from tweepy import Stream
from tweepy.streaming import StreamListener

################################################################################


class TweetListener(StreamListener):

    def on_data(self, data):
        try:
            with open('../tweets.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True


if __name__ == "__main__":

    # parse arguments
    parser = argparse.ArgumentParser(description='Argument for Tweet Text')
    parser.add_argument('text', help="Tweet Text to Search")
    args = parser.parse_args()


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

        twitter_stream = Stream(auth, TweetListener())
        twitter_stream.filter(track=[args.text])

