#!/usr/bin/env python3

import tweepy
import random
import os
from credentials import *
from config import TWEET_PATH, IMAGE_PATH, STATIC_HASHTAG1, STATIC_HASHTAG2


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
    messages = open(TWEET_PATH).read().splitlines()
    message = ' '.join([random.choice(messages),random.choice(messages),random.choice(messages)])
    photo = random.choice(os.listdir(IMAGE_PATH))
    filename = os.path.join(IMAGE_PATH, photo)
    return filename, message

# Publish tweet
def sendTweet(filename, message):
    media = api.media_upload(filename)
    api.update_status(status=message, media_ids=[media.media_id])


#Main routine
authentication = setAuthenticationParams()
api = loginToTwitter(authentication)
filename, message = generateTweet()
sendTweet(filename, message)
