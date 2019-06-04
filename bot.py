import tweepy
import time

consumer_key = 'YWp8HSCkWGYGA6cAX97mdyqGv'
consumer_secret = '1ZCVID6yjczBQ1eVZUISUz8H2DwS9zoXXT4UWR3RNtSjYW2e7s'

key = '1037008788690231298-kWUK6NzmJ7HnJXtW8mBSDhw1WlCjSb'
secret = 'Ofg1LoId3klScjnZvQAI442k84OqCjNGgQhXcrLxBQbRy'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)

FILE_NAME = 'last_seen.txt'

def read_last_seen(FILE_NAME):
    file_name = open(FILE_NAME,'r')
    last_seen_id = int(file_name.read().strip())
    file_name.close()
    return last_seen_id

def store_last_seen(FILE_NAME,last_seen_id):
    file_write = open(FILE_NAME,'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return

def reply():
    tweets = api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode='extended')
    for tweet in tweets:
        print('Retweeted To - ' + str(tweet.user.screen_name) + tweet.full_text)
        api.create_favorite(tweet.id)
        api.retweet(tweet.id)
        store_last_seen(FILE_NAME,tweet.id)

while True:
    reply()
    time.sleep(5)

