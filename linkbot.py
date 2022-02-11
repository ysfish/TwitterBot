#!/usr/bin/env python3

import tweepy
import random
import os
from credentials import *
from config import LINK_PATH, STATIC_HASHTAG1, STATIC_HASHTAG2

# Authenticate to Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create API object
api = tweepy.API(auth)

# Create a tweet
messages = open(LINK_PATH).read().splitlines()
message = ' '.join(['STATIC_HASHTAG1','STATIC_HASHTAG2',random.choice(messages),random.choice(messages),random.choice(messages),random.choice(messages)])
api.update_status(status=message)
