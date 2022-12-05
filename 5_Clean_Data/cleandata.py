
import pandas as pd


keyword = input("Please enter lowercase CashTag of the coin to perform clean process (btc,ada,doge,eth,iota,xmr,ankr): ")

dfclean = pd.read_csv(f'C:/Users/conni/Documents/Dissertation Data/4_Join_Data/{keyword}_final.csv')

print(f'pre clean shape {dfclean.shape}')

dfclean = dfclean.dropna()

dfclean = dfclean.drop(labels=['symbol_id','time_period_end', 'time_open', 'time_close', 'sx_sum'],axis=1) 

print(f'post clean shape {dfclean.shape}')

print(dfclean.head())

dfclean.to_csv(f'C:/Users/conni/Documents/Dissertation Data/5_Clean_Data/{keyword}_clean_data.csv',index=False)