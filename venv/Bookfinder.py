from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import sqlite3

conn3 = sqlite3.connect('sellers.db')


pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
page = requests.get("https://www.bookfinder.com/search/?keywords=3791355228&currency=USD&destination=us&mode=basic&classic=off&ps=tp&lang=en&st=sh&ac=qr&submit=").text
soup = bs(page, 'html.parser')
#for tag in soup.find_all(True):
    #print(tag.name)

tables = soup.find_all(attrs={"class": "results-table-Logo"})
sellers = soup.find(attrs={"class": "results-explanatory-text-Logo"})

for table in tables,:
    #print(table)
    df_new = pd.read_html(str(table))[0]
    df_used = pd.read_html(str(table))[1]
    #print('DFNEW', df_new)
    #print('DFUSED', df_used)
    name = soup.select(".results-table-LogoRow has-data")
    print(name)
#print(len(tables))
#print(soup.prettify())
#print(df_new.loc[1])
df_new.to_csv('C:/Users/gratt/PycharmProjects/Scraping_bookfinder/file.csv')
df_new.to_sql(name='sellers_df', con=conn3, index=False, if_exists='append')

