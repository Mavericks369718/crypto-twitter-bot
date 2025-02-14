import tweepy
import os

# Get API keys from GitHub Secrets
consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

# Authenticate with Twitter
client = tweepy.Client(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)

# Post a test tweet using API v2
response = client.create_tweet(text="Hello, Crypto World! 🚀 #Crypto #Bitcoin")

print("Tweet posted successfully! Response:", response)



