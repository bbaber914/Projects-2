from bs4.element import TemplateString
import requests
from bs4 import BeautifulSoup

print("Current Weather Search:")
city = input("Please enter the city you would like to search: ")
state = input("What State is that city in? ")
city = "Youngstown"
state = "Ohio"

url = f"https://www.google.com/search?q=weather+{city}+{state}"
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")
print(soup.title)


current_temp = soup.find_all("div", class_="BNeawe iBp4i AP7Wnd")
high_temp = soup.find_all("div", attrs={"class": "gNCp2e", "class": "gNCp2e"})
print(current_temp)
print(high_temp)

for item in current_temp:
        print(item.text)

print("#####################################")
print(f"The current temperature in {city}, {state} is {current_temp[0].text}.")
print("#####################################")
for div in current_temp:
         print(div.text)
print("#####################################")


# for items in soup.find_all('a'):
#         print(items.get('href'))
