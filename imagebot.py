#!/usr/bin/env python3

import tweepy
import random
import os
from credentials import *
from config import TWEET_PATH, IMAGE_PATH

# Authenticate to Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create API object
api = tweepy.API(auth)

# Create a tweet
messages = open(TWEET_PATH).read().splitlines()
message = ' '.join(['STATIC_HASHTAG1','STATIC_HASHTAG2',random.choice(messages),random.choice(messages),random.choice(messages)])
photo = random.choice(os.listdir(IMAGE_PATH))
filename = os.path.join(IMAGE_PATH, photo)
media = api.media_upload(filename)
api.update_status(status=message, media_ids=[media.media_id])
