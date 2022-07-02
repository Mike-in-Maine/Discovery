import concurrent.futures
import ftplib
import functools
import os
import datetime
import time
import random
import pandas as pd
import sqlalchemy
import asyncio
import pathlib as pl2

engine = sqlalchemy.create_engine('mysql+pymysql://miky1973:itff2020@mysql.irish-booksellers.com:3306/irishbooksellers')
download_path = "C:/Users/gratt/Dropbox/inventory/inventory"
files = os.listdir(download_path)

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
df = pd.DataFrame()

ps = pl2.Path(download_path)
dfs = (pd.read_csv(p, sep='\t', index_col=False, on_bad_lines='skip')for p in ps.glob('*.*'))
df = pd.concat(dfs, ignore_index=True)
#Bad way to
#for filename in files:
#    local_filename = os.path.join(download_path, filename)
#    dd = pd.read_csv(local_filename, sep='\t', index_col=False, on_bad_lines='skip')
#    df = pd.concat([df, dd], ignore_index=True)

    #print(len(df))
#print('Working on file:', filename)
    #df.to_sql(name='inventorydownload', con=engine, index=False, if_exists='append')


print('Done concat')
##print('With duplicates:', df.count())
df.drop_duplicates(subset='listingid', keep='first', inplace=True)
df.sort_values(by=['Price'], inplace=True, ignore_index=True)
##print(df.count())
#df.to_csv('C:/Users/gratt/Dropbox/inventory/inventory/latest/all.csv')
df.to_sql(name='inventorydownload', con=engine, index=False, if_exists='replace')

#asyncio.run(main())