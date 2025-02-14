import tweepy
import os

# Get API keys from GitHub Secrets
consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

# Authenticate with Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Post a test tweet
api.update_status("Hello, Crypto World! 🚀 #Crypto #Bitcoin")
print("Tweet posted successfully!")
