from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import sqlite3
import pandas as pd
import requests
import xml.etree.ElementTree as ET
import xmltodict, json
import untangle
import sqlalchemy
from tkinter import font
import re
import urllib

engine = sqlalchemy.create_engine('mysql+pymysql://miky1973:itff2020@mysql.irish-booksellers.com:3306/irishbooksellers')
root = Tk()
root.title('Learn radio buttons')
root.geometry("600x1200")
root.config(bg='#9FD996')
conn = sqlite3.connect('orders_database.db')
c = conn.cursor()

c.execute("SELECT * FROM new_orders")
records = c.fetchall()
number_orders = 0
order_numbers = ''
ship_to_names = ''
ship_to_countrys = ''

for record in records:
    order_numbers += str(record[1]) + "\n"
    ship_to_names += str(record[2]) + "\n"
    ship_to_countrys += str(record[3]) + "\n"
#print(len(records))
f = font.Font(size=9)
number_orders = Label(root, text="You have " + str(len(records)) + " new orders to process" ,bg='#9FD996',font= 'Helvetica')
number_orders['font'] = f
number_orders.grid(row=0, column=1, columnspan=20, sticky='w')

order = Label(root, text=order_numbers, bg='#9FD996', font="Helvetica", )
order['font'] = f
order.grid(row=1, column=1, sticky='e',)

name = Label(root, text=ship_to_names)
name['font'] = f
name.grid(row=1, column=2, sticky='w')

country = Label(root, text=ship_to_countrys)
country['font'] = f
country.grid(row=1, column=3)

#check_bookfinder()

#print(records)

#f_name = Entry(root, width=30)
#f_name.grid(row = 0, column = 1, padx = 20)
#f_name_label = Label(root, text='First name')
#f_name_label.grid(row=0, column=1)

#c.execute("CREATE TABLE orders")
def check_bookfinder(isbns):
    #cursor = sqlalchemy.create_engine
    df = pd.DataFrame()
    for book_finder_isbn in isbns:
        # url1 = 'https://www.amazon.com/Crosshairs-Deception-Ken-Reamy/dp/1606472399/ref=sr_1_1?crid=17JEYCW765CEG&keywords=1606472399&qid=1649268063&s=books&sprefix=1606472399%2Cstripbooks%2C47&sr=1-1'
        #url1 = f'https://www.bookfinder.com/search/?author=&title=&lang=en&isbn={book_finder_isbn}&new_used=*&destination=us&currency=USD&mode=basic&st=sr&ac=qr'
        url1 = f'https://www.amazon.com/s?k={book_finder_isbn}'

        url = urllib.parse.quote(url1)
        #print(url)
        response = requests.get("http://api.scrape.do?token=9c904d30b8d747ee93dcfe615ac0552e0cb72ba2d82&url=" + url)
        df = pd.read_html(response.text)
        #print(df)
        #print(type(url))
        print(response.text)


def get_abe_API_neworders(): #Connects to Abe api, gets new orders, puts them in a sqlite3 database by replacing the one that is there.
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    df = pd.DataFrame()
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
    title = []
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
            print(string)
            pattern_new = '^M|_11|_4$'
            if re.sub()
            isbns.append(string)

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



    #for zip in codes:
    #    labelNumberOfOrders = Label(text=zip, font=('bold', 2))
    #    labelNumberOfOrders
    #for phone in phones:
    #    labelphone = Label(text=phone, font=('bold', 2), fg='red')#.grid(column=1, row=0, padx=5, pady=5)
    #    labelphone.pack()
    #for street in streets:
    #    labelstreet = Label(text=street, font=('bold', 2))#.grid(column=2, row=0, padx=5, pady=5)
    #    labelstreet.pack()

    dict = {'ISBN': isbns, 'SHIPTONAME': names, 'SHIPTOCOUNTRY': countrys}

    df = pd.DataFrame(dict)
    print(df)
    conn3 = sqlite3.connect('orders_database.db')
    #df.to_sql(name='new_orders', con=engine, index=False, if_exists='append')
    df.to_sql(name='new_orders', con = conn3, if_exists='replace') #creates/updates the database locally in sqlite3

get_abe_API_neworders()



conn.commit()
conn.close()
mainloop()


