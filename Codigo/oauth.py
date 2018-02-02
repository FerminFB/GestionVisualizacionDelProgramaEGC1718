#-*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

import tweepy

# == OAuth Authentication ==
#
# This mode of authentication is the new preferred way
# of authenticating with Twitter.

# page located at https://dev.twitter.com/apps (under "OAuth settings")
consumer_key="mTSMT3SgEJNQcWFCYCenWACqs"
consumer_secret="2ssH7SErBEYW1F6Gc0ByvBD0AjGf2sYlRTJvNjMBRdCIrbz25T"

# The access tokens can be found on your applications's Details
# page located at https://dev.twitter.com/apps (located
# under "Your access token")
access_token="392627830-xuY08mATOmAotrjITfLxMX1J9FJjZ8Hd73kgy0LZ"
access_token_secret="RZcootqGzwrcUEMJHn6eIPsnv8YvSOPpxAgEf9Q25GhAj"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# If the authentication was successful, you should
# see the name of the account print out
print(api.me().name)

# If the application settings are set for "Read and Write" then
# this line should tweet out the message to your account's
# timeline. The "Read and Write" setting is on https://dev.twitter.com/apps
api.update_status(status='Updating using OAuth authentication via Tweepy!')
