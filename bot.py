import tweepy
import os
import requests

# Get API keys from GitHub Secrets
consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

# Authenticate with Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Fetch Bitcoin price from CoinGecko API
def get_crypto_price(crypto="bitcoin"):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto}&vs_currencies=usd"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data[crypto]["usd"]
    return None

# Generate tweet
bitcoin_price = get_crypto_price()
if bitcoin_price:
    tweet = f"🚀 Bitcoin Price Update: ${bitcoin_price} USD 💰\n#Bitcoin #Crypto"
    api.update_status(tweet)
    print("Tweet posted successfully:", tweet)
else:
    print("Failed to fetch crypto price.")



