import math
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler 
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

lstmdata = pd.read_csv(f'C:/Users/conni/Documents/Dissertation Data/5_Clean_Data/ada_clean_data.csv')
xticksdta = lstmdata['time_period_start']
lstmdata.set_index('time_period_start',drop=True,inplace=True)

print(lstmdata.head())


close_prices = lstmdata['px_close']
values = close_prices.values
training_data_len = math.ceil(len(values)* 0.8)

scaler = MinMaxScaler(feature_range=(0,1))
scaled_data = scaler.fit_transform(values.reshape(-1,1))
train_data = scaled_data[0: training_data_len, :]

x_train = []
y_train = []

for i in range(10, len(train_data)):
    x_train.append(train_data[i-10:i, 0])
    y_train.append(train_data[i, 0])
    
x_train, y_train = np.array(x_train), np.array(y_train)
x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))

test_data = scaled_data[training_data_len-10: , : ]
x_test = []
y_test = values[training_data_len:]

for i in range(10, len(test_data)):
  x_test.append(test_data[i-10:i, 0])

x_test = np.array(x_test)
x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))


model = keras.Sequential()
model.add(layers.LSTM(100, return_sequences=True, input_shape=(x_train.shape[1], 1)))
model.add(layers.LSTM(100, return_sequences=False))
model.add(layers.Dense(25))
model.add(layers.Dense(1))
model.summary()

model.compile(optimizer='adam', loss='mean_squared_error')
model.fit(x_train, y_train, batch_size= 1, epochs=10)


predictions = model.predict(x_test)
predictions = scaler.inverse_transform(predictions)
rmse = np.sqrt(np.mean(predictions - y_test)**2)
print(f'RMSE {rmse}')

data = lstmdata.filter(['px_close'])
train = data[:training_data_len]
validation = data[training_data_len:]
validation['Predictions'] = predictions




plt.figure(figsize=(16,8))
plt.title('Xmr Predictions vs Actual Price')
plt.xlabel('Date')
plt.ylabel('Close Price USD ($)')
plt.plot(train)
plt.plot(validation[['px_close', 'Predictions']])
plt.legend(['Train', 'Val', 'Predictions'], loc='lower right')
ratio= xticksdta.size
quarter = round((ratio/100)*25)
half = round((ratio/100)*50)
threeqarter = round((ratio/100)*75)
plt.xticks([xticksdta[0],
            xticksdta[quarter],
            xticksdta[half],
            xticksdta[threeqarter],
            xticksdta[ratio -1]])


plt.savefig(f'/content/drive/MyDrive/5_Clean_Data/xmr_lstm.png')

plt.show()