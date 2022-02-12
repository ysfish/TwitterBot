#!/usr/bin/env python3

import tweepy
import random
import os
from credentials import *
from config import LINK_PATH, STATIC_HASHTAG1, STATIC_HASHTAG2

# Authenticate to Twitter
def setAuthenticationParams():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    return auth

# Create API object and authenticate to twitter API
def loginToTwitter(auth):
    api = tweepy.API(auth)
    return api

# Create a tweet
def generateTweet():
    messages = open(LINK_PATH).read().splitlines()
    message = ' '.join([random.choice(messages),random.choice(messages),random.choice(messages),random.choice(messages)])
    return message

#Main Routine
authentication = setAuthenticationParams()
api = loginToTwitter(authentication)
message = generateTweet()
api.update_status(status=message)
