
#import libraries
import string
import csv
import pandas as pd
#import seaborn as sns
import matplotlib.pyplot as mp
#create a corpus file.
badwords = []
for line in open("badwords.txt"):
    for word in line.split( ):
        badwords.append(word)

import tweepy
from tweepy import OAuthHandler

# set up api keys

consumer_key = 'LZgYZq2aR3YCB4C1vxfPuKXIH'
consumer_secret = 'qAPu1AG5neHs48KalGYxL3YwCaWOcj0ZDvsCu0HjealIACGd5x'
access_token = '1396766344302010371-DYzdr3sinziMOvuKyp1ZnhxBegDng7'
access_token_secret = '798RfbNlTjn7Pc4GajyAY9GA8V93D9MqMq3QgAqzRDXs7'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

#@title Default title text
search_value = "chatbot_t" #@param {type:"string"}

mytweet = tweepy.Cursor(api.search,q=search_value +'-filter:retweets', tweet_mode= "extended")
#mytweet= tweepy.Cursor(api.home_timeline, tweet_mode= "extended")
csvfile=open(search_value + '_test.csv', 'a')
csvWriter=csv.writer(csvfile)

for status in mytweet.items():
    print ("tweet: "+ str(status.full_text.encode('utf-8)')))
    tweet = status.full_text
    tweet = "".join(l for l in tweet if l not in string.punctuation)
    tweet = tweet.lower()
    bullying = "False"
    for word in tweet.split(" "):
        if word in badwords:
            bullying = "True"
            print (bullying)
            break
    if bullying == "False":
        print (bullying)
    row = tweet +","+ bullying + "\n"
    csvWriter.writerow([tweet,bullying])

df=pd.read_csv("tweets.csv")
db=pd.read_csv("dataa.csv")
df = df.astype(str)
col= ['Tweets','Classification']
df.columns=col
df.head()