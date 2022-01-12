import requests
from bs4 import BeautifulSoup

target_link = "https://www.target.com/p/hidden-valley-original-ranch-salad-dressing-38-topping-gluten-free-16-fl-oz/-/A-13105486#lnk=sametab"
walmart_link = 'https://www.walmart.com/ip/Hidden-Valley-Original-Ranch-Salad-Dressing-Topping-Gluten-Free-16-oz-Bottle/10451460?athbdg=L1200'

headers = {"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}

page = requests.get(url=target_link, headers=headers)
soup = BeautifulSoup(page.content,'lxml')
print(soup.prettify())
title = soup.find(id = 'productTitle')
text = title.get_text() 
product_title = text.strip() 
print(product_title )
price = soup.find(id = 'priceblock_ourprice')
price = price.get_text() 
target_product_price = price.strip() 
print(target_product_price )

page = requests.get(url=walmart_link, headers=headers)
soup = BeautifulSoup(page.content,'lxml')
print(soup.prettify())
title = soup.find(id = 'productTitle')
text = title.get_text() 
product_title = text.strip() 
print(product_title )
price = soup.find(id = 'priceblock_ourprice')
price = price.get_text() 
walmart_product_price = price.strip() 
print(walmart_product_price )

tag = soup.find('span', class_ = 'price') 
text = tag.get_text() 
target_product_price = text.strip() 
target_product_price

tag = soup.find('span', class_ = 'price') 
text = tag.get_text() 
walmart_product_price = text.strip() 
walmart_product_price

import pickle
def storeData():
   target = {'key' : 'target', 'product_name' : 'hidden valley original ranch', 'price' : target_product_price}
   walmart = {'key' : 'walmart', 'product_name' : 'Hidden Valley Original Ranch', 'price' : walmart_product_price}

   db = {}
   db['target'] = target
   db['walmart'] = walmart

    
   dbfile = open('price_data', 'ab')
    
   pickle.dump(db, dbfile)                    
   dbfile.close()

   def read_data():
    dbfile = open('price_data', 'rb')    
   sb_store = pickle.load(dbfile)
   for items in db_store:
       print(items, ' :: ', db[items])
   dbfile.close()
