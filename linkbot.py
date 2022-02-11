#!/usr/bin/env python3

import tweepy
import random
import os
from credentials import *
from config import LINK_PATH

# Authenticate to Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create API object
api = tweepy.API(auth)

# Create a tweet
messages = open(LINK_PATH).read().splitlines()
message = random.choice(messages)
api.update_status(status=message)
