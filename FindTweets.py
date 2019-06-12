#!/usr/bin/python

################################################################################
import tweepy
import json
import argparse

################################################################################
if __name__ == "__main__":

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

        api = tweepy.API(auth)

        public_tweets = api.home_timeline()
        for tweet in public_tweets:
            print(tweet.text)
