import pandas as pd 
import datetime
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.statespace.sarimax import SARIMAX

btc = pd.read_csv(f'C:/Users/conni/Documents/Dissertation Data/4_Join_Data/iota_final.csv')

btc['time_period_start'] = pd.to_datetime(btc['time_period_start'], format= '%Y/%m/%d')

sns.set()
plt.ylabel('BTC Price')
plt.xlabel('Date')
plt.xticks(rotation=45)

btc.index = btc['time_period_start']

#plt.plot(btc.index, btc['px_close'], )
#plt.show()
#print('tried')



# & btc.index < "2019-08-31"
test = btc[btc.index > "2021-08-01"]
train = btc[(btc.index < "2021-08-01")   ]# & (btc.index > "2019-05-01" )

test.index = pd.to_datetime(test['time_period_start'], format= '%Y/%m/%d')
train.index = pd.to_datetime(train['time_period_start'], format= '%Y/%m/%d')

#btc.drop('time_period_start')
#test.drop('time_period_start')
#train.drop('time_period_start')

plt.plot(train['px_close'],  color = "black", label = 'Train')
plt.plot(test['px_close'],  color = "red", label = 'Test')
plt.ylabel('BTC Price')
plt.xlabel('Date')
plt.xticks(rotation=45)
plt.title("Train/Test split for BTC Data")
#plt.show() 

#print(test.head())
#print(train.head())

target = train['px_close'] 
'''
ARMAmodel = SARIMAX(target, order = (1, 0, 1))
ARMAmodel = ARMAmodel.fit()

target_pred = ARMAmodel.get_forecast(len(test.index))
target_pred_df = target_pred.conf_int(alpha = 0.05) 
target_pred_df["Predictions"] = ARMAmodel.predict(start = target_pred_df.index[0], end = target_pred_df.index[-1])
target_pred_df.index = test.index.to_period('D')
target_pred_out = target_pred_df["Predictions"] 

plt.plot(target_pred_out, color='green', label = 'Predictions')
#plt.legend()'''
#plt.show()
#10,0,30
ARIMAmodel = ARIMA(target, order = (10, 0,30))
ARIMAmodel = ARIMAmodel.fit()

y_pred = ARIMAmodel.get_forecast(len(test.index))
y_pred_df = y_pred.conf_int(alpha = 0.05) 
y_pred_df["Predictions"] = ARIMAmodel.predict(start = y_pred_df.index[0], end = y_pred_df.index[-1])
y_pred_df.index = test.index
y_pred_out = y_pred_df["Predictions"] 

plt.plot(y_pred_out, color='Yellow', label = 'ARIMA Predictions')
plt.legend()
plt.show()