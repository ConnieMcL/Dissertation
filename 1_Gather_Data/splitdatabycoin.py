import pandas as pd
import csv

maindf = pd.read_csv(r'C:\Users\conni\Documents\alldata.csv')

listofcoins=['BINANCE_SPOT_ADA_USDT','BINANCE_SPOT_ANKR_USDT','BINANCE_SPOT_BTC_USDT','BINANCE_SPOT_DOGE_USDT','BINANCE_SPOT_ETH_USDT','BINANCE_SPOT_IOTA_USDT','BINANCE_SPOT_XMR_USDT']

trimmeddf = maindf[maindf.symbol_id.isin(listofcoins)]


#trimmeddf.to_csv(r'C:\Users\conni\Documents\trimmeddata.csv',index=False)


tfcardanodf = trimmeddf.symbol_id.isin(['BINANCE_SPOT_ADA_USDT'])
tfanchordf = trimmeddf.symbol_id.isin(['BINANCE_SPOT_ANKR_USDT'])
tfbitcoindf = trimmeddf.symbol_id.isin(['BINANCE_SPOT_BTC_USDT'])
tfdogedf = trimmeddf.symbol_id.isin(['BINANCE_SPOT_DOGE_USDT'])
tfetherdf = trimmeddf.symbol_id.isin(['BINANCE_SPOT_ETH_USDT'])
tfiotadf = trimmeddf.symbol_id.isin(['BINANCE_SPOT_IOTA_USDT'])
tfxmrdf = trimmeddf.symbol_id.isin(['BINANCE_SPOT_XMR_USDT'])



cardanodf = trimmeddf[tfcardanodf]
anchordf = trimmeddf[tfanchordf]
bitcoindf = trimmeddf[tfbitcoindf]
dogedf = trimmeddf[tfdogedf]
etherdf = trimmeddf[tfetherdf]
iotadf = trimmeddf[tfiotadf]
xmrdf = trimmeddf[tfxmrdf]


cardanodf.to_csv(r'C:\Users\conni\Documents\ADAdata.csv',index=False)
anchordf.to_csv(r'C:\Users\conni\Documents\ANKRdata.csv',index=False)
bitcoindf.to_csv(r'C:\Users\conni\Documents\BTCdata.csv',index=False)
dogedf.to_csv(r'C:\Users\conni\Documents\DOGEdata.csv',index=False)
etherdf.to_csv(r'C:\Users\conni\Documents\ETHdata.csv',index=False)
iotadf.to_csv(r'C:\Users\conni\Documents\IOTAdata.csv',index=False)
xmrdf.to_csv(r'C:\Users\conni\Documents\XMRdata.csv',index=False)