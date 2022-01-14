import requests
from bs4 import BeautifulSoup
import smtplib

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
   global target
   target = {'key' : 'target', 'product_name' : 'hidden valley original ranch', 'price' : target_product_price}
   global walmart
   walmart = {'key' : 'walmart', 'product_name' : 'Hidden Valley Original Ranch', 'price' : walmart_product_price}

   global db
   db = {}
   db['target'] = target
   db['walmart'] = walmart

    
   dbfile = open('price_data', 'ab')
    
   pickle.dump(db, dbfile)                    
   dbfile.close()

def read_data():
    dbfile = open('price_data', 'rb')    
    db_store = pickle.load(dbfile)
    for items in db_store:
       print(items, ' :: ', db[items])
    dbfile.close()

target_product_price = float(target_product_price[1:])
walmart_product_price = float(walmart_product_price[1:])

min_price = min (target_product_price,walmart_product_price)

if min_price == target_product_price:
 Company = target
 URL = target_link
elif min_price == walmart_product_price:
 Company = walmart
 URL = walmart_link

def notifications():
 server = smtplib.SMTP("smtp.gmail.com",587)
 server.ehlo()
 server.starttls()
 server.ehlo()
 server.login("username","password")
 subject = "Prices Fell Down"

 body = "Please check {company} , click her {url}".formay(company = Company, url = URL)
 msg = f"Subject:{subject}, \n\n{body}"
 server.sendmail("receivermailid",msg)

 print("mail send")
 server.quit()
