from textblob import TextBlob
import sys
import tweepy
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
#from config import API_KEY, API_SECRET_KEY,BEARER_KEY,ACESS_TOKEN,ACESS_SECRET_TOKEN # This line replaces the lines that set the variables.

from PIL import Image
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from langdetect import detect
from nltk.stem import SnowballStemmer
from nltk.sentiment.vader import SentimentIntensityAnalyzer





#Sentiment Analysis
def percentage(part,whole):
 return 100 * float(part)/float(whole)

keyword = input("Please enter lowercase CashTag of the coin to perform sentiment (btc,ada,doge,eth,iota,xmr,ankr): ")

df = pd.read_csv(f'C:/Users/conni/Documents/Dissertation Data/2_Tweet_Data/{keyword}_tweet_data.csv')


tweets = df['text']
noOfTweet = tweets.size

processcount=0

positive = 0
negative = 0
neutral = 0
polarity = 0
tweet_list = []
neutral_list = []
negative_list = []
positive_list = []
sentiment_score_list = []
sentiment_pnn_list =[]


for tweet in tweets:
 
 print(f'processing : {processcount}')
 processcount+= 1
 #print(tweet.text)
 sent_text='neutral'

 tweet_list.append(tweet)
 analysis = TextBlob(tweet)
 score = SentimentIntensityAnalyzer().polarity_scores(tweet)

 sentiment_score_list.append(score)

 neg = score['neg']
 neu = score['neu']
 pos = score['pos']
 comp = score['compound']
 polarity += analysis.sentiment.polarity
 
 if comp>=0.05:
    sent_text='positive'

 if comp<= -0.05:
    sent_text= 'negative'

 sentiment_pnn_list.append(sent_text)

 if neg > pos:
    negative_list.append(tweet)
    negative += 1
 elif pos > neg:
    positive_list.append(tweet)
    positive += 1
 
 elif pos == neg:
    neutral_list.append(tweet)
    neutral += 1

# if processcount == 105:
#    break

positive = percentage(positive, noOfTweet)
negative = percentage(negative, noOfTweet)
neutral = percentage(neutral, noOfTweet)
polarity = percentage(polarity, noOfTweet)
positive = format(positive, '.1f')
negative = format(negative, '.1f')
neutral = format(neutral, '.1f')



tweet_list = pd.DataFrame(tweet_list)
neutral_list = pd.DataFrame(neutral_list)
negative_list = pd.DataFrame(negative_list)
positive_list = pd.DataFrame(positive_list)
print("total number: ",len(tweet_list))
print("positive number: ",len(positive_list))
print("negative number: ", len(negative_list))
print("neutral number: ",len(neutral_list))



sentiment_list= pd.DataFrame(sentiment_score_list)

#sentiment_list['overall'] = sentiment_pnn_list
sentiment_list['date'] = df['created_at']


sentiment_list.to_csv(f'C:/Users/conni/Documents/Dissertation Data/3_Sentiment_Data/{keyword}_sentiment_data.csv',index=False)