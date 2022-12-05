
import pandas as pd 
import datetime
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import xgboost as xgb
from xgboost import plot_importance
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns

#coin =''

data = pd.read_csv(f'C:/Users/conni/Documents/Dissertation Data/5_Clean_Data/doge_clean_data.csv')

data.index = data['time_period_start']
xticksdta = data['time_period_start']
data = data.drop(columns='time_period_start')

X, y = data,data['px_close']
X = X.drop(columns="px_close")

print(X.head())

print(y.head())

#data_dmatrix = xgb.DMatrix(data=X,label=y)

#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123)

X_train = X[(X.index < "2021-08-02")]
X_test = X[(X.index > "2021-08-02")]
y_train = y[(y.index < "2021-08-02")]
y_test = y[(y.index > "2021-08-02")]



xg_reg = xgb.XGBRegressor(objective ='reg:squarederror', #reg:squarederror reg:linear
                        colsample_bytree = 0.3, 
                        learning_rate = 0.3,
                        max_depth = 2, 
                        alpha = 0.1, 
                        n_estimators = 50)

xg_reg =xg_reg.fit(X_train,y_train)
preds = xg_reg.predict(X_test)

predsdf = pd.DataFrame(preds)
predsdf.index= y_test.index
print(y_train.head())
print(y_test.head(-5))
print(predsdf.head())

rmse = np.sqrt(mean_squared_error(y_test, preds))
print("RMSE: %f" % (rmse))

sns.set()
plt.ylabel('Price')
plt.xlabel('Date')
plt.xticks(rotation=45)
plt.title("Train/Test/Predictions split for Doge")

plt.plot(y_train,  color = "black", label = 'Train')
plt.plot(y_test,  color = "red", label = 'Test')
plt.plot(predsdf, color='Yellow', label = 'Predictions')
#plt.xticks(fontsize=5)
#print(f'this thing {xticksdta.size}')
ratio= xticksdta.size
quarter = round((ratio/100)*25)
half = round((ratio/100)*50)
threeqarter = round((ratio/100)*75)

#y.index[0],y.index[-1],y[round((ratio/100)*50]
#['2017-01-01','2018-01-01', '2019-01-01', '2020-01-01', '2021-01-01' ]
plt.xticks([xticksdta[0],
            xticksdta[quarter],
            xticksdta[half],
            xticksdta[threeqarter],
            xticksdta[-1]])

plt.legend()
plt.show()


plot_importance(xg_reg)
plt.title("Feature Importance Eth")
plt.show()