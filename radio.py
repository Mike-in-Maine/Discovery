import itertools
from tkinter import *
import bs4
from PIL import ImageTk, Image
from tkinter import filedialog
import sqlite3
import pandas as pd
import requests
from requests_html import HTMLSession
from requests_html import HTML
import xml.etree.ElementTree as ET
import xmltodict, json
import untangle
import sqlalchemy
from tkinter import font
import re
import webbrowser
import urllib
import colorama
from lxml import etree
from colorama import Fore
from itertools import count
from bs4 import BeautifulSoup as bs
import time
import pyautogui

def getWeight_one(x):
    #url1 = f'https://www.amazon.com/dp/{x}'
    #url = urllib.parse.quote(url1)
    print("WORKINK ON:", x)
    #print(url1)
    #response = requests.get("http://api.scrape.do?token=9c904d30b8d747ee93dcfe615ac0552e0cb72ba2d82&url="+url).text
    #print(response)
    #soup = bs(response, 'lxml')
    #print(soup)

    #try:
    #    match = html.xpath('// *[ @ id = "detailBulletsWrapper_feature_div"]')
    #    match2 = html.xpath('//*[@id="detailBullets_feature_div"]/ul/li[6]/span/span[2]')
    #    #weight = match[0].text
    #    weight2 = match2[0].text
    #    print('From Amazon: ', weight)
    #    print('From Amazon: ', Fore.LIGHTYELLOW_EX + weight2 + Fore.RESET)
    #except Exception as e: weight = "Amazon - UNK ", print(e)

    #Gets weight from isbndb.com
    try:
        h = {'Authorization': '46481_38467d2795da46fd550a9b402a4018bc'}
        resp = requests.get(f"https://api2.isbndb.com/book/{x}", headers=h).text
        json_dict = json.loads(resp)
        print('\n____________________________')
        print('ISBNDB.com ', json_dict['book']['dimensions'])
        print('____________________________')

    except KeyError as isbnbd: weight_isbndb = 'ISBNDB.com = UNK', print(isbnbd)
def getWeight_all():
    weights = []
    conn3 = sqlite3.connect('orders_database.db')
    df = pd.read_sql('SELECT * FROM new_orders',con=conn3)
    #cursor = conn3.cursor()
    #print(df)
    col_one_list = df['ISBN'].tolist()
    for isbn in col_one_list:
        try:
            h = {'Authorization': '46481_38467d2795da46fd550a9b402a4018bc'}
            resp = requests.get(f"https://api2.isbndb.com/book/{isbn}", headers=h).text
            json_dict = json.loads(resp)
            weight_line = json_dict['book']['dimensions']

            #weights.append(weight_only)
            weights.append(json_dict['book']['dimensions'])
            #print(weight_only[0])
        except KeyError as isbnbd:
            weights.append('UNK')
    #weights_only = []
    #for i in weights:
    #    weight_only = re.findall(r"(?<=Weight: )\d+.\d+ \w+", i)
    #    weights_only.append(weight_only)

    df['WEIGHTS'] = weights
    df.to_sql(name='new_orders', con=conn3, index=False, if_exists='replace')
def get_abe_API_neworders(): #Connects to Abe api, gets new orders, puts them in a sqlite3 database by replacing the one that is there.
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    df = pd.DataFrame()
    df1 = pd.DataFrame()
    data = """
    <?xml version="1.0" encoding="ISO-8859-1"?>
    <orderUpdateRequest version="1.1">
        <action name="getAllNewOrders">
            <username>irishbooksellers</username>
            <password>ef624a8bd5a843cda651</password>
        </action>
    </orderUpdateRequest>
    """
    headers = {'username': 'irishbooksellers', 'password': 'ef624a8bd5a843cda651'}
    response = requests.get('https://orderupdate.abebooks.com:10003', data=data, headers=headers)
    #print(response.text)

    root = ET.fromstring(response.text)
    dump = xmltodict.parse(response.text)

    obj = untangle.parse(response.text)
    emails = []
    cities = []
    codes = []
    countrys = []
    names = []
    phones = []
    regions = []
    streets = []
    street2s = []
    buyer_purchase_order_ids = []
    domain_ids= []
    domain_names = []
    order_days = []
    titles = []
    # to add:
    order_months = []
    order_years = []
    order_hour= []
    order_minute = []
    order_seconds = []
    shipping_currency = []
    subtotal_currency = []
    total_currency = []
    purchase_order_item_ids = []
    book_id = []
    author = []
    description = []
    isbns = []
    isbn_clean=[]

    vendor_key = []
    stsus_code = []
    extra_item_shipping = []
    first_item_shipping = []
    new_used= []
    max_delivery_days = []
    min_deliver_days = []
    tracking = []
    shipping_company = []

    for po in root.findall('purchaseOrderList'):
        for itemid in po.iter('buyerPurchaseOrder'):
            buyerPurchaseOrder = itemid.get('id')
            buyer_purchase_order_ids.append(buyerPurchaseOrder)
        for domain_id in po.iter('domain'):
            domain = domain_id.get('id')
            domain_ids.append(domain)

        for domain2 in po.iter('domain'):
            domain_name = domain2.find('name').text
            domain_names.append(domain_name)

        for po5 in po.iter('book'):
            isbn = po5.find('vendorKey').text
            pattern = r'^M|_11|_4$'
            string = re.sub(pattern, '', isbn)
            #print(string)
            pattern_new = '_4$'
            if re.search(pattern_new, isbn):
                new_used.append("used")
                #print(isbn, " is used")
            else:
                new_used.append("new")
                #print(isbn, " is new" )
            isbns.append(string)
            title = po5.find('title').text
            titles.append(title)

        for order_date in po.iter('orderDate'):
            for date in order_date.iterfind('date'):
                order_day = date.find('day').text
                order_days.append(order_day)
                order_month = date.find('month').text
                order_months.append(order_month)
                order_year = date.find('year').text
                order_years.append(order_year)

        for po2 in po.findall('purchaseOrder'):

            for po3 in po2.findall('buyer'):
                for purchaseOrder in po2.iter('purchaseOrder'):
                    purchase_order_item_id = purchaseOrder.get('id')
                #for total in po2.findall('orderTotals'):
                    #print("total = ",total.text) #Doesnt work

                for po5 in po3.findall('email'):
                    emails.append(po5.text)
                for po4 in po3.findall('mailingAddress'):
                    city = po4.find('city').text
                    code = po4.find('code').text
                    country = po4.find('country').text
                    name = po4.find('name').text
                    phone = po4.find('phone').text
                    region = po4.find('region').text
                    street = po4.find('street').text
                    street2 = po4.find('street2').text

                    purchase_order_item_ids.append(purchase_order_item_id)

                    cities.append(city)
                    codes.append(code)
                    countrys.append(country)
                    names.append(name)
                    phones.append(phone)
                    regions.append(region)
                    streets.append(street)
                    street2s.append(street2)

    print(purchase_order_item_ids)
    print(buyer_purchase_order_ids)
    print(cities)
    print(codes)
    print(countrys)
    print(phones)
    print(names)
    print(regions)
    print(streets)
    print(street2s)
    print(emails)
    print(domain_ids)
    print(domain_names)
    print(order_days)
    print(order_months)
    print(order_years)
    print(isbns)
    print(new_used)
    print(titles)
    #check_bookfinder(isbns)
    #to add:

    print(len(buyer_purchase_order_ids))
    print(len(cities))
    print(len(codes))
    print(len(countrys))
    print(len(names))
    print(len(phones))
    print(len(regions))
    print(len(streets))
    print(len(street2s))
    print(len(purchase_order_item_ids))
    print(len(domain_ids))
    print(len(domain_names))
    print(len(order_days))
    print(len(order_months))
    print(len(order_years))
    print(len(isbns))
    print(len(new_used))
    print(len(titles))




    #for zip in codes:
    #    labelNumberOfOrders = Label(text=zip, font=('bold', 2))
    #    labelNumberOfOrders
    #for phone in phones:
    #    labelphone = Label(text=phone, font=('bold', 2), fg='red')#.grid(column=1, row=0, padx=5, pady=5)
    #    labelphone.pack()
    #for street in streets:
    #    labelstreet = Label(text=street, font=('bold', 2))#.grid(column=2, row=0, padx=5, pady=5)
    #    labelstreet.pack()

    dict = {'ABEPOID':purchase_order_item_ids, 'ISBN': isbns, 'CONDITION': new_used, 'SHIPTONAME': names, 'SHIPTOADDRESS': streets, 'SHIPTOADDRESS2': street2s, 'SHIPTOCITY': cities, 'SHIPTOPROVSTATE': regions, 'SHIPTOZIPCODE': codes, 'SHIPTOCOUNTRY': countrys, 'TITLE': titles, 'BUYEREMAILADDRESS': emails}

    df = pd.DataFrame(dict)
    print(df)
    conn3 = sqlite3.connect('orders_database.db')
    engine = sqlalchemy.create_engine('mysql+pymysql://miky1973:itff2020@mysql.irish-booksellers.com:3306/irishbooksellers')
    df.to_sql(name='new_orders', con=conn3, index=False, if_exists='replace')
    #df.to_sql(name='new_orders', con = engine, if_exists='replace') #creates/updates the database locally in sqlite3
    ## TODO take all the ISBNs and strat checking availability on bookfinder by calling 'def check_bookfinder(isbns):'
    #getWeight(isbns)
## TODO def get_abe_FTP_neworders():
def scrape_bookfinder_data():
    #take data from local database orders_database
    conn3 = sqlite3.connect('orders_database.db')
    df_orders = pd.read_sql("SELECT ISBN FROM new_orders", conn3)
    isbns = df_orders["ISBN"].tolist()
    for isbn in isbns:
        HEADERS = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'
        #time.sleep(3)

        page = requests.get(f"https://www.bookfinder.com/search/?keywords={isbn}&currency=USD&destination=us&mode=basic&classic=off&ps=tp&lang=en&st=sh&ac=qr&submit=", headers=HEADERS)
def get_weight(obj_order):
    h = {'Authorization': '46481_38467d2795da46fd550a9b402a4018bc'}
    resp = requests.get(f"https://api2.isbndb.com/book/{obj_order}", headers=h)
    print(resp.json())
    return resp.json()
def check_bookfinder(isbns):
    #cursor = sqlalchemy.create_engine
    df = pd.DataFrame()
    for book_finder_isbn in isbns:
        # url1 = 'https://www.amazon.com/Crosshairs-Deception-Ken-Reamy/dp/1606472399/ref=sr_1_1?crid=17JEYCW765CEG&keywords=1606472399&qid=1649268063&s=books&sprefix=1606472399%2Cstripbooks%2C47&sr=1-1'
        url1 = f'https://www.bookfinder.com/search/?author=&title=&lang=en&isbn={book_finder_isbn}&new_used=*&destination=us&currency=USD&mode=basic&st=sr&ac=qr'
        #url1 = f'https://www.amazon.com/s?k={book_finder_isbn}'

        url = urllib.parse.quote(url1)
        #print(url)
        response = requests.get("http://api.scrape.do?token=9c904d30b8d747ee93dcfe615ac0552e0cb72ba2d82&url=" + url)
        df = pd.read_html(response.text)
        #print(df)
        #print(type(url))
        #print(response.text)

get_abe_API_neworders()
getWeight_all()

engine = sqlalchemy.create_engine('mysql+pymysql://miky1973:itff2020@mysql.irish-booksellers.com:3306/irishbooksellers')
root = Tk()

root.title('Learn radio buttons')
root.geometry("600x1200")
root.config(bg='#9FD996')
conn = sqlite3.connect('orders_database.db')
c = conn.cursor()

c.execute("SELECT * FROM new_orders")
records = c.fetchall()
print(records[0])
number_orders = 0
order_numbers = ''
ship_to_names = ''
ship_to_countrys = ''
weight_obj = ''
ship_to_address1 = ''
ship_to_address2 = ''
ship_to_zip = ''
ship_to_state = ''


for record in records:
    single_order = str(record[1])
    order_numbers += str(record[2]) + "\n"
    ship_to_names += str(record[3]) + "\n"
    ship_to_countrys += str(record[4]) + "\n"
    weight_obj += str(record[5]) + "\n"
#print(len(records))

#weights_only = re.findall(r"(?<=Weight: )\d+[.]\d+ \w+", weight_obj)



f = font.Font(size=8)
border = 1
number_orders = Label(root, text="You have " + str(len(records)) + " new orders to process" ,bg='#9FD996',font= 'Helvetica',border = 1)
number_orders['font'] = f
number_orders.grid(row=0, column=0, columnspan=20, sticky='w', pady=10)

for count, record in enumerate(records):
    obj_order = record[0]
    obj_isbn = record[1]
    obj_condition = record[2]
    obj_name = record[3]
    obj_title = record[10]
    obj_country = record[9]
    obj_weight = record[12]
    #print(record[4])
    row = count+1
    #weight = get_weight(obj_order)
    #print(obj_order)

    order = Button(root, text = obj_order, command=lambda x=obj_isbn: open_biblio_url(x))
    order['font'] = f
    order.grid(row=row, column=0, sticky='e')

    process_biblio = Button(root, text = 'BBL', command = lambda x=obj_order: process_from_BIBLIO(x), bg = '#C17A6B')
    process_biblio['font'] = f
    process_biblio.grid(row=row, column=1, sticky='w')

    if obj_condition == 'used':
        condition = Label(root, text=obj_condition, foreground='#f29d5c', background='#9FD996')
    else:
        condition = Label(root, text=obj_condition, bg='#9FD996')
    condition['font'] = f
    condition.grid(row=row, column=2, sticky='w')

    title = Label(root, text=obj_title, bg='#9FD996')
    title['font'] = f
    title.grid(sticky='w', row=row, column=3)

    #name = Label(root, text=obj_name, bg='#9FD996')
    #name['font'] = f
    #name.grid(row=row, column=2, sticky='w')

    country = Label(root, text=obj_country, bg='#9FD996')
    country['font'] = f
    country.grid(sticky='e', row=row, column=7)

    #obj_weight1 = re.findall(r"(?<=Weight: )\d+[.]\d+ \w+", obj_weight)
    weight = Label(root, text=obj_weight, bg='#9FD996')
    weight['font'] = f
    weight.grid(sticky='w', row=row, column=4)

    r1 = Radiobutton(root, text="PRCS", value=0, variable=1)
    r2 = Radiobutton()
    r1.grid(sticky='w', row=row, column=8)

    #weight_book = Label(root, text=weight, bg='#9FD996')
    #weight_book['font'] = f
    #weight_book.grid(sticky='e', row=row, column=4)

def open_biblio_url(x):
    url1 = (f'https://www.bookfinder.com/search/?author=&title=&lang=en&isbn={x}&new_used=*&destination=us&currency=USD&mode=basic&st=sr&ac=qr')
    url = urllib.parse.quote(url1)
    webbrowser.open_new("http://api.scrape.do?token=9c904d30b8d747ee93dcfe615ac0552e0cb72ba2d82&url=" + url)

def process_from_BIBLIO(x):
    conn = sqlite3.connect('orders_database.db')
    #c = conn.cursor()
    #c.execute("SELECT * FROM new_orders")
    #records = c.fetchall()
    #print(records)
    df = pd.read_sql(f"SELECT * FROM new_orders WHERE ABEPOID is {x}", con = conn)
    ship_to_name = df.iloc[0]['SHIPTONAME']+" {NO INVOICE}"
    print(ship_to_name)
    res = pyautogui.locateOnScreen('pictures/biblio/proceed_to_checkout.PNG')

    pyautogui.click(res)
    go_to_checkout = pyautogui.center(res)
    time.sleep(1)
    pyautogui.moveTo(go_to_checkout)
    time.sleep(1)
    pyautogui.click()

    print(df)

    conn.close()


root.update_idletasks()
conn.commit()
conn.close()

mainloop()


