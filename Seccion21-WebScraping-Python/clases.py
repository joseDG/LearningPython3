import requests
import bs4

res = requests.get('https://es.wikipedia.org/wiki/Grace_Murray_Hopper')
soup = bs4.BeautifulSoup(res.text, "lxml")

# Soup

first_item = soup.select('.toctext')[0]

for item in soup.select('.toctext'):
    print(item.text)
