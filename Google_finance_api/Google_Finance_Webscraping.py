import requests

import pandas as pd
from bs4 import BeautifulSoup
BASE_URL = "https://www.google.com/finance/quote/TSLA:NASDAQ?hl=en"
INDEX = "TSLA:NASDAQ"
SYMBOL = "TSLA"
LANGUAGE = "en"
TARGET_URL = f"{BASE_URL}/quote/{SYMBOL}:{INDEX}?hl={LANGUAGE}"

# make an HTTP requests

page = requests.get(TARGET_URL)

# use an HTML Parser to grab the content from "Page"

soup= BeautifulSoup(page.content, "html.parser")

# get the item that describe the stock

items = soup.find_all("div", {"class": "gyFHrc"})

# create a dictionary to store the stock description

stock_description = {}

# iterate over the items and append them to the dictionary

for item in items:
    item_description = item.find("div", {"class":"mfs7Fc"}).text
    item_value = item.find("div",{"class":"P6K39c"}).text
    stock_description[item_description]=item_value

# print(stock_description")
#print(stock_description["Dividend yield"])


# Convert the stock description dictionary to a Dataframe

df =pd.DataFrame(list(stock_description.items()),columns=['Description','Value'])

#write the DataFrame to an Excel file

df.to_excel("Stock_Data.xlsx",index=False)



