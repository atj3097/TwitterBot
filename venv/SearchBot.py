import tweepy
import tkinter
import time
consumer_key = 'YvpQz2Ej8Q6yCyfAhYVasq70f'
consumer_secret = 'WtPP9ZqEMb0tQIRzLSubfxLcsEZisYn0zCdohAUxoT4MmCbffD'
access_token = '2533772329-tEh3070zt6vQsbjPB4onCzoyNkSn1yE11ieJM3F'
access_token_secret = 'qXYu063ExhEFKE6zV4lcCQII1uzepuN99R5CZlrLsaFeh'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

hashtag = "#SaySo"
tweetNumber = 2

tweets = tweepy.Cursor(api.search, hashtag).items(tweetNumber)

def searchBot():
    for tweet in tweets:
        try:
            tweet.retweet()
            print("Retweet")
            time.sleep(10)
        except tweepy.TweepError as e:
            print(e.reason)
            time.sleep(10)

searchBot()