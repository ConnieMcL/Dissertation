import pandas as pd
import csv

distinct_vals = pd.read_csv(r'C:\Users\conni\Documents\realdata.csv')

list_of_exchange = distinct_vals['symbol_id'].unique()



#for bean in list_of_exchange:
#    print(bean)


with open(r'C:\Users\conni\Documents\unique_exchange.csv', 'w') as f:
      
    # using csv.writer method from CSV package
    write = csv.writer(f)
      
    write.writerow(list_of_exchange)
    

print(len(list_of_exchange))