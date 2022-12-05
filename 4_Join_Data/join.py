import pandas as pd



keyword = input("Please enter lowercase CashTag of the coin to perform join (btc,ada,doge,eth,iota,xmr,ankr): ")

dfprice = pd.read_csv(f'C:/Users/conni/Documents/Dissertation Data/1_Price_Data/{keyword}_data.csv')

dfsentiment = pd.read_csv(f'C:/Users/conni/Documents/Dissertation Data/3_Sentiment_Data/{keyword}_sentiment_daily_sentiment_score.csv')


dfprice['time_period_start'] = pd.to_datetime(dfprice['time_period_start']).dt.date
dfsentiment['date'] = pd.to_datetime(dfsentiment['date']).dt.date
dfsentiment.columns = dfsentiment.columns.str.replace('date', 'time_period_start')


print(dfprice.head())
print(dfsentiment.head())






result = pd.merge(dfprice, dfsentiment, how="outer", on= ['time_period_start'])

print(result.head())

result.to_csv(f'C:/Users/conni/Documents/Dissertation Data/4_Join_Data/{keyword}_final.csv',index=False)
