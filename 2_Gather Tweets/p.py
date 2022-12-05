
import datetime
import requests
import os
import json
import pandas as pd
import time



keyword = input("Please enter lowercase CashTag of the coin to perform sentiment (btc,ada,doge,eth,iota,xmr,ankr): ")

searchdict={'btc':'$BTC Bitcoin -RT',
            'xmr':'$XMR Monero -RT',
            'eth':'$ETH Ethereum -RT',
            'doge':'$DOGE Doge -RT',
            'ada':'$ADA Cardano -RT',
            'ankr':'$ANKR Ankr -RT',
            'iota':'$IOTA Iota -RT'}
            
            
daterangedf= pd.read_csv(f'C:/Users/conni/Documents/Dissertation Data/1_Price_Data/{keyword}_data.csv')


max_date = pd.to_datetime(daterangedf['time_period_start']).max()
min_date = pd.to_datetime(daterangedf['time_period_start']).min()

print(f'maxdate{max_date}')
print(f'min_date {min_date}')
'''
endtweetdate = datetime.date(max_date)
starttweetdate= datetime.date(min_date)
'''
enddate = max_date
startdate= min_date

delta= enddate - startdate
deltadays = delta.days

tweetdate = str(min_date).split(' ')[0]

print(tweetdate)

#endDF=pd.DataFrame(columns=['created_at','text'])