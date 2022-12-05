import os 
import zipfile
import pandas as pd

rootdir =r'C:\Users\conni\Documents\Price Data'

endDF=pd.DataFrame(columns=['symbol_id','time_period_start','time_period_end','time_open','time_close','px_open','px_high','px_low','px_close','sx_cnt','sx_sum'])

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        #print os.path.join(subdir, file)
        filepath = subdir + os.sep + file
        #print(f'This is the file: {filepath}')

        df = pd.read_csv(filepath,delimiter=';',compression='gzip')
        print(df.head())
        endDF =pd.concat([endDF, df])
        #endDF = endDF.concat(df, ignore_index = True)
        #del df

endDF.to_csv(r'C:\Users\conni\Documents\realdata.csv',index=False)


    
