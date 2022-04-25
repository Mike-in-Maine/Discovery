import requests
#import urllib2
import re
from requests.auth import HTTPProxyAuth
import pandas as pd
import csv
import itertools
import re
from fp.fp import FreeProxy
from fake_useragent import UserAgent
from random import randint
import time
from Numspy import Way2sms


def checkone():

    ua = UserAgent()
    useragent = {'User-Agent': ua.random}
    print(useragent)
    amz_url = "https://www.bookfinder.com/search/?keywords=0615636993&currency=USD&destination=us&mode=basic&classic=off&ps=tp&lang=en&st=sh&ac=qr&submit="
    for loop in range(1,5):
        with open('C:/Users/gratt/Desktop/proxies.csv', newline='') as f:
            reader = csv.reader(f)
            proxy_list = list(reader)
            print(proxy_list)
            ips = []
            for ip in proxy_list:
              for ip2 in ip:
                ips.append(ip2)
        print(ips)

        #proxyfree = FreeProxy(rand=True).get()
        #print(proxyfree)
        s = requests.Session()
        faild_conn = 0

        for proxy in ips:
          proxies = {
           "http": proxy
          }
          print(proxy)
          auth = HTTPProxyAuth("gomcodoc", "gomcomike")

          s.proxies = proxies
          s.auth = auth        # Set authorization parameters globally
          print("Trying ", proxy)

          try:
            time.sleep(randint(0,6))
            ext_ip = s.get(amz_url, timeout= 5, headers=useragent)
          except:
            print('didnt connect')
            faild_conn+=1
            continue
          print (ext_ip.text)
          print("failed: ", faild_conn)



w2s = Way2sms()
w2s.login(Way2sms_Username, Way2sms_Password)
w2s.send(2076890047, 'YAY!!!')
w2s.logout()