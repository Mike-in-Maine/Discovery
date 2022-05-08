import pandas as pd
import numpy as np
import json
import requests
import xml.etree.ElementTree as ET
from lxml.etree import fromstring


df = pd.read_xml('C:/Users/gratt/Dropbox/inventory/xml_inventory/file10.xml')
print(df)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

df = pd.read_xml('C:/Users/gratt/Dropbox/inventory/xml_inventory/file10.xml')
#print(df)
df_dhl = pd.read_csv('C:/Users/gratt/Dropbox/inventory/ShippingRatesFiles/csv/DHL.csv')
df_ids = pd.read_csv('C:/Users/gratt/Dropbox/inventory/ShippingRatesFiles/csv/IDS.csv')
df_apc = pd.read_csv('C:/Users/gratt/Dropbox/inventory/ShippingRatesFiles/csv/APCDDU.csv')
w = 96

country = 'ES'
try:
    print('DHL:',df_dhl.loc[w][country])
    print('IDS:', df_ids.loc[w][country] + 1.80 + 1.60 + 0.10, '\n', 'DHL:', df_dhl.loc[w][country], '\n', 'APC:',df_apc.loc[w][country])
except:
    pass


#github

#payload = {b'<?xml version="1.0" encoding="ISO-8859-1"?><orderUpdateRequest version="1.1"><action name="getAllNewOrders"><username>irishbooksellers</username><password>ef624a8bd5a843cda651</password></action></orderUpdateRequest'}

#response = requests.get('https://orderupdate.abebooks.com:10003', data=payload)
#print(response.content)
#get_all_new_orders = {b'<?xml version="1.0" encoding="ISO-8859-1"?><orderUpdateRequest version="1.1"><action name="getAllNewOrders"><username>irishbooksellers</username><password>ef624a8bd5a843cda651</password></action></orderUpdateRequest>'}
#response = requests.get('https://orderupdate.abebooks.com:10003', headers={'username':'irishbooksellers', 'password':'ef624a8bd5a843cda651'}, data=get_all_new_orders)
#print(response.content)
#text = ET.parse(response)
#print(text.tag)
#all_orders_df = pd.DataFrame()
#import libraries


#load shipping grids for the following:
#IDS = weigh per pound/10 (fractions of pound) + per PC + 1.60 Processing fee + 0.13 fuel surcharge
#APC = grid DDP no tracking

