import os
import tweepy as tw
import pandas as pd
import csv
import re 
import string
import preprocessor as p
consumer_key= 'OkiOx2qanOrjAeGIgGYoZpzyS'
consumer_secret= 'Am1lo0ZreYVIuv6XJKQnxFbDpKv5QS971gY1hwwQi9AR8HfG5T'
access_token= '1511628444114640899-NnZX0fGOoEFiLo2VFW7iN5j0NMSbc0'
access_token_secret= 'ZqHbrTnh0ET4h6i0cUCZLNt8RG7vYzAZ0FGtLCUASor83'
auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)
csvFile = open('file-name', 'a')
csvWriter = csv.writer(csvFile)

search_words = "#WildLife"      # enter your words
new_search = search_words + " -filter:retweets"

for tweet in tw.Cursor(api.search,q=new_search,count=100,
                           lang="en",
                           since_id=0).items():
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8'),tweet.user.screen_name.encode('utf-8'), tweet.user.location.encode('utf-8')])
