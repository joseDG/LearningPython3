from bs4 import BeautifulSoup
import requests
import lxml
import pandas as Pandas
from openpyxl.workbook import Workbook


url="https://www.flipkart.com/ckf/czl/~cs-1zk8p4dgbr/pr?sid=ckf,czl&collection-tab-name=Large+Screen+TVs-DT&wid=8.productCard.PMU_V2_4"


data = requests.get(url=url)

final_data = data.content

soup = BeautifulSoup(final_data, "lxml")
soup.prettify()

### Price of TV after Discount ###
name = soup.findAll(class_="_30jeq3 _1_WHN1")
tv_prices = []
for price in name:
    final_price  = price.text
    tv_prices.append(final_price)


### Company of TV  ###
names = soup.findAll(class_="_4rR01T")
tv_names = []
features = []


for name in names:
    final_name  = name.text.split()

    tv_names.append(final_name[0])

for feat in names:
    feature  = feat.text.split()

    features.append(feature)





### Price of TV before  Discount ###

actual_pric = soup.findAll(class_="_3I9_wc _27UcVY")
actual_price = []
for price in actual_pric:
    first_price  = price.text
    actual_price.append(first_price)



###  Discount Percentage ###

dis = soup.findAll(class_="_3Ay6Sb")
discount = []
for percent in dis:
    discount_percent  = percent.text.split()

    discount.append(discount_percent[0])


### Product Rating###
rating = soup.findAll(class_="_3LWZlK")
final_rating = []
for star in rating:
    current_rating = star.text

    final_rating.append(current_rating)




data = [tv_names, actual_price, discount, tv_prices,  features,  final_rating]
df = Pandas.DataFrame(data)
df.index = ["TV NAMES", "ACTUAL PRICE", "DISCOUNT", "CURRENT_PRICE", "FEATURES", "RATING"]
excel = df.to_csv("products_data.csv")