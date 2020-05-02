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
FILE_NAME = '/Users/god/PycharmProjects/TwitterBot/venv/last_seen.txt'
# api.update_status('Testing Twitter Bot')

#reading from file for last seen tweet id
def read_last_seen(FILE_NAME):
        file_read = open('last_seen.txt', 'r')
        last_seen_id = int(file_read.read().strip())
        file_read.close()
        return  last_seen_id

#writing
def store_last_seen(FILE_NAME, last_seen_id):
    file_write = open('last_seen.txt', 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return


def reply():
    tweets = api.mentions_timeline(read_last_seen('last_seen.txt'))
    for tweet in tweets:
        if 'adamthebot' in tweet.text.lower():
            print(tweet.text)
            api.update_status("@" + tweet.user.screen_name + " Stay Safe Bitch Ass Nigga! Get a life loser!", tweet.id)
            api.create_favorite(tweet.id)
            api.retweet(tweet.id)
            store_last_seen('last_seen.txt', tweet.id)

while True:
    reply()
    time.sleep(5)