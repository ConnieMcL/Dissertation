import tweepy
from tweepy.parsers import JSONParser

consumerKey = 'iuZzlbHZBOTqYFCdE61zp7en3'
consumerSecret = 'OmEO4SlBccpHyXReQ2G1PY3LB4LW3pVQjNQuZWf1TxvmTrcHPv'
accessToken = '850063319272759296-ft2VtkyFZlAaMiskV3SNeDI7GTXpNHy'
accessTokenSecret = 'woe9mNjmHshhKUogKco7abZcywJKj7XOiUW5jBB8tN4UY'
auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)


#new_tweet = api.search_tweets(q="beans", count=1)
new_tweet = tweepy.Cursor(api.search_tweets, q="beans").items(1)

#print(f'Time of tweet : {new_tweet.created_at}')
#print(f'Body of tweet : {new_tweet.text}')
#print(f'{new_tweet["statuses"]} ')

for tweet in new_tweet: 
    print(tweet.text)