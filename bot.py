import tweepy

# Twitter API credentials (replace these with your keys)
consumer_key = "your_consumer_key"
consumer_secret = "your_consumer_secret"
access_token = "your_access_token"
access_token_secret = "your_access_token_secret"

# Authenticate with Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Post a test tweet
api.update_status("Hello, Crypto World! 🚀 #Crypto #Bitcoin")
print("Tweet posted successfully!")
