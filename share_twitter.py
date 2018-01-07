from __future__ import absolute_import, print_function

import tweepy

# Go to http://apps.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key="mTSMT3SgEJNQcWFCYCenWACqs"
consumer_secret="2ssH7SErBEYW1F6Gc0ByvBD0AjGf2sYlRTJvNjMBRdCIrbz25T"

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token="392627830-xuY08mATOmAotrjITfLxMX1J9FJjZ8Hd73kgy0LZ"
access_token_secret="RZcootqGzwrcUEMJHn6eIPsnv8YvSOPpxAgEf9Q25GhAj"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
api.update_status('Hello world https://institucional.us.es/innosoft/ #isoftdays #test vía @InnoSoftDays')


