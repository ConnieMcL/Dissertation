import pandas as pd


keyword = input("Please enter lowercase CashTag of the coin to perform clean process (btc,ada,doge,eth,iota,xmr,ankr): ")

dfcat = pd.read_csv(f'C:/Users/conni/Documents/Dissertation Data/5_Clean_Data/{keyword}_clean_data.csv')

print(dfcat.head())


position = 0



higher_lower=[]
pricelist = dfcat['px_close'].to_list()




for i in pricelist:
    #print(f'Todays price = {pricelist[position]}, tomorrow = {pricelist[position +1]}')
    try:    
        if pricelist[position] < pricelist[position+ 1]:
            higher_lower.append('Higher')
        else:
            higher_lower.append('Lower')

        position+=1
    
    except:
        break

#print(higher_lower)
higher_lower.append('Lower')
dfcat['tomorow_high_low'] = higher_lower

dfcat.to_csv(f'C:/Users/conni/Documents/Dissertation Data/7_Categorize_Data/{keyword}_cat_data.csv',index=False)

#dfcatprint(higher_lower)