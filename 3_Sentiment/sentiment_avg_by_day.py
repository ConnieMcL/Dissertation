import pandas as pd






keyword = input("Please enter lowercase CashTag of the coin to perform sentiment (btc,ada,doge,eth,iota,xmr,ankr): ")

df = pd.read_csv(f'C:/Users/conni/Documents/Dissertation Data/3_Sentiment_Data/{keyword}_sentiment_data.csv')

df['date'] = pd.to_datetime(df['date']).dt.floor('d')


dfgroup = df.groupby(['date'])['compound'].mean().to_frame('avg_score').reset_index()


print(df.head())
print(dfgroup.head())


dfgroup.to_csv(f'C:/Users/conni/Documents/Dissertation Data/3_Sentiment_Data/{keyword}_sentiment_daily_sentiment_score.csv',index=False)