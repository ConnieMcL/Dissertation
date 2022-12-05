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

#def calc_date_range():



def bearer_oauth(r):

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

    keyword = input("Please enter lowercase CashTag of the coin to perform sentiment (btc,ada,doge,eth,iota,xmr,ankr): ")

    searchdict={'btc':'$BTC Bitcoin -RT',
                'xmr':'$XMR Monero -RT',
                'eth':'$ETH Ethereum -RT',
                'doge':'$DOGE Doge -RT',
                'ada':'$ADA Cardano -RT',
                'ankr':'$ANKR Ankr -RT',
                'iota':'$IOTA Iota -RT'}

    #daterangedf= pd.read_csv(f'C:/Users/conni/Documents/Dissertation Data/1_Price_Data/{keyword}_data.csv')
    
    daterangedf= pd.read_csv(f'C:/Users/conni/Documents/Dissertation Data/1_Price_Data/{keyword}_data.csv')
    
    max_date = pd.to_datetime(daterangedf['time_period_start']).max()
    min_date = pd.to_datetime(daterangedf['time_period_start']).min()

    #print(f'maxdate{max_date}')
    #print(f'min_date {min_date}')

    enddate = max_date
    startdate= min_date

    delta= enddate - startdate
    deltadays = delta.days
    
    endDF=pd.DataFrame(columns=['created_at','text'])
    
    tweetdate = min_date
    
    

    for i in range(1,deltadays):

        
        tweetdate = tweetdate + datetime.timedelta(days=1)
        start_date= str(tweetdate).split(' ')[0] + 'T00:00:00Z'
        querystring=searchdict[keyword]

        query_params = {'query': querystring ,
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

            break
            '''
            print('Sleeping 16 mins')
            time.sleep(960)
            print('Sleep over')
            '''


    #f'C:/Users/conni/Documents/Dissertation Data/1_Price_Data/{keyword}_data.csv'
    endDF.to_csv(f'C:/Users/conni/Documents/Dissertation Data/2_Tweet_Data/{keyword}_data.csv',index=False)







if __name__ == "__main__":
    main()