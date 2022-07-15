from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import regex
import sqlite3
import urllib
from urllib import parse
import urllib.parse
from urllib.parse import urlparse
from datetime import datetime
from fake_useragent import UserAgent
#user = UserAgent.load()
conn3 = sqlite3.connect('sellers.db')


pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
x = '0147509181'
#url1 = f"https://www.bookfinder.com/search/?keywords={x}&currency=USD&destination=us&mode=basic&classic=off&ps=tp&lang=en&st=sh&ac=qr&submit="
#url1 = 'https://www.bookfinder.com/search/?author=&title=&lang=en&new_used=*&destination=us&currency=USD&binding=*&isbn=0810914220&keywords=0810914220&minprice=&maxprice=&publisher=&min_year=&max_year=&mode=advanced&st=sr&ac=qr'
#f'https://www.bookfinder.com/search/?keywords={x}&currency=USD&destination=us&mode=basic&classic=off&ps=tp&lang=en&st=sh&ac=qr&submit='
url1 = f'https://www.bookfinder.com/search/?author=&title=&lang=en&isbn={x}&destination=us&currency=USD&mode=basic&st=sr&ac=qr'

url = urllib.parse.quote(url1)
#print(url)
page = requests.get("http://api.scrape.do?token=9c904d30b8d747ee93dcfe615ac0552e0cb72ba2d82&url="+url)
#print(page.text)
#page = requests.get("https://www.bookfinder.com/search/?keywords=0895581639&currency=USD&destination=us&mode=basic&classic=off&ps=tp&lang=en&st=sh&ac=qr&submit=")
page2 = page.text
soup = bs(page2, 'lxml')
#for tag in soup.find_all(True):
    #print(tag.name)
prices = []
sellers = []
titles = []
marketplace = []

tables = soup.find_all(attrs={"class": "results-table-Logo"}) #Finds the 2 tables new and used
marketplace_used = str(tables[1])
#print(marketplace_used)
marketplace_new = str(tables[0])
#print(marketplace_new)
#print(len(marketplace_new))

prices_bs = tables[1].find_all(attrs={'class':'results-price'})
#print(prices_bs)
sellers_bs = tables[1].find_all(attrs={'class':'results-explanatory-text-Logo'})

marketplaces_bs = (tables[1]).find_all('img', alt=True)
for foo in marketplaces_bs:
   marketplace.append(foo["alt"])
   print(foo)

for price in prices_bs:
    item = price.get_text()
    prices.append(item)
#print(prices)

for seller in sellers_bs[0::3]: #this notion is wrong and breaks at TextBookX
    item2 = seller.get_text()
    sellers.append(item2)
    print(seller)

for market in tables:
    marketplace.append(market)
#print(marketplace)

for title in marketplaces_bs[2:]: #The first 2 are not sellers
    titles.append(title.get('title'))


print(prices) #These are new and used
print(titles)
print(sellers)

#sellers = soup.find(attrs={"class": "results-explanatory-text-Logo"})
print('prices', len(prices))
print('sellers', len(titles))
print('marketplaces', len(marketplace))

dict = {'Marketplaces': titles, 'Sellers': marketplace, 'Prices': prices}
df = pd.DataFrame(dict)
#print(df)
df.to_sql(name='sellers_df', con=conn3, index=False, if_exists='replace')


#df_new.to_csv('C:/Users/gratt/PycharmProjects/Scraping_bookfinder/file.csv')
#df_new.to_sql(name='sellers_df', con=conn3, index=False, if_exists='replace')

###________ This entire part tries to get data by reading an html with pandas and it doesnt work well
tables = soup.find_all(attrs={"class": "results-table-Logo"})

#print("first",tables[1])
#marketplace_used = pd.read_html(str(tables[1]))
#marketplace_new = pd.read_html(str(tables[0]))
#print(type(marketplace_new))
#print("NEWWWWWWWWW:", marketplace_new[0])
#print("USEDDDDDDDD:",marketplace_used)

df2_new = marketplace_new[0]
df2_new.to_sql(name='sellers_db', con=conn3, index=False, if_exists='replace')

#print(marketplace_new)
#print(type(marketplace_new[0]))#This is a dataframe not a list
#print(len(marketplace_used))#This is a list of dataframes
#print(type(tables))
#sellers_bs = soup.find_all(attrs={'class':'results-explanatory-text-Logo'})

#for title in marketplaces_bs[2:]: #The first 2 are not sellers
    #titles.append(title.get('title'))
    #print(title)

df_tables = []
for table in tables:
    #print (table.text)
    marketplaces_used = table.text
    #marketplaces_used = table.findAll("img", {"title": regex.compile(r".*")})
    print('Marketplaces used', marketplaces_used)

    df_count_tables = pd.read_html(table_html)
    #print(df_count_tables)
    df_count_tables.insert(5, 'ISBN', x)# inserts the ISBN column
    df_count_tables.insert(6, 'CONDITION', 'new')
    df_count_tables.insert(7, 'TIMESTAMP', datetime.today())

    df_tables.append(df_count_tables)
    #print(df_new)#(str(table))[0]
    #df_used = pd.read_html(str(table))
    #df_mkplc_new = pd.DataFrame(titles)
   # print(df_new)
    #print(df_mkplc_new)
    #regex = ".+?(?=via)"

    #df_new.insert(3, 'MARKETPLACE', titles)

    #print('DFNEW', df_new)
    #print('DFUSED', df_used)

    #dict = {'Marketplaces': titles, 'Sellers': sellers, 'Prices': prices}
    #df = pd.DataFrame(dict)
    # print(df)
for hack in df_tables:
    print(hack)
#df_used.to_sql(name='sellers_df', con=conn3, index=False, if_exists='append')
#df_new.to_sql(name='sellers_df', con=conn3, index=False, if_exists='append')
    #name = soup.select(".results-table-LogoRow has-data")

    #print(name)
#print(len(tables))
#print(soup.prettify())
#print(df_new.loc[1])
###_________

    print('111111111111111', table[0])
    print(len(table[0]))
    print('222222222222222', table[1])
    print(len(table[1]))
    print("JEHNYY", str(table[1]))
