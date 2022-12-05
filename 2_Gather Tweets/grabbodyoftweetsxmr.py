import datetime
import requests
import os
import json
import pandas as pd
import time

# To set your environment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAFjvZQEAAAAADqY4JycZGGjy1rk%2BfpnHsP9T%2Bsk%3DcLmFzcvmnXmQxWLANiQi2XZmYtR9GWv2BCubSs5O1tpWdcp8dA'

search_url = "https://api.twitter.com/2/tweets/search/all"

#test = '2017-08-19T00:00:00Z'
# Optional params: start_time,end_time,since_id,until_id,max_results,next_token,
# expansions,tweet.fields,media.fields,poll.fields,place.fields,user.fields
#tweetdate= datetime.date(2018,5,31)


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2FullArchiveSearchPython"
    return r


def connect_to_endpoint(url, params):
    response = requests.request("GET", search_url, auth=bearer_oauth, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


def main():

    tweetdate= datetime.date(2019,3,15)
    endDF=pd.DataFrame(columns=['created_at','text'])
#for i in range(1,1638):
    for i in range(1,1066):

        
        tweetdate = tweetdate + datetime.timedelta(days=1)
        start_date= str(tweetdate) + 'T00:00:00Z'


        query_params = {'query': '$XMR MONERO Monero -RT',
                    'tweet.fields': 'id,text,created_at',
                    'max_results':101,
                    'end_time': {start_date}}



        json_response = connect_to_endpoint(search_url, query_params)


    
        tweet_data = json_response['data']

        df = pd.json_normalize(tweet_data)

        endDF =pd.concat([endDF, df])
        time.sleep(1.5)
        print(f'added {i} values')
        if (i % 297 == 0):
            print('Sleeping 16 mins')
            time.sleep(960)
            print('Sleep over')




    endDF.to_csv(r'C:\Users\conni\Documents\xmr_tweet_data.csv',index=False)







if __name__ == "__main__":
    main()
