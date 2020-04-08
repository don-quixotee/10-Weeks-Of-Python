import pandas as pd
import requests
from bs4 import BeautifulSoup as sp



response = requests.get("https://www.flipkart.com/mobiles/pr?sid=tyy,4io&marketplace=FLIPKART")
print(response)
soup = sp(response.content, "html.parser")
Name_list = []
Price_list = []
Rating_list = []

for i in range(1,51):
    link = soup.find("a",text = "Next").get("href")
    home_page_url = "https://www.flipkart.com"
    next_page_link = home_page_url + link[:-1]+str(i)
    response2 = requests.get(next_page_link)
    
    soup2 = sp(response2.content, "html.parser")
    cards = soup2.find_all("div", attrs = {"class": "_1UoZlX"})
    
    for card in cards:
        name = card.find("div", attrs = {"class": "_3wU53n"})
        price = card.find("div",attrs= {"class":"_2rQ-NK"})
        rating = card.find("div",attrs = {"class":"hGSR34"})
        
        if name:
            name_text = name.text
        else:
            name_text = None
        if price:
            price_text = price.text
        else:
            price_text = None
        if rating:
            rating_text = rating.text
        else:
            rating_text = None
        # print(i,"{} {} {}".format(name_text, price_text, rating_text))
        Name_list.append(name_text)
        Price_list.append(price_text)
        Rating_list.append(rating_text)
    

mobile_data = pd.DataFrame(
  {  "Names" : Name_list,
    "Prices" : Price_list,
    "Ratings": Rating_list
  }
)
 
print(mobile_data)
mobile_data.to_csv('mobileData.csv')
# mobile_data.to_numpy('data.npy')
# mobile_data.to_excel('mobileData.xls')
# mobile_data.to_excel("data.xls")
