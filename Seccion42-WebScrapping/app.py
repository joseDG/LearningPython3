import requests
from bs4 import BeautifulSoup

r = requests.get('https://pythonizing.github.io/data/example.html')
c = r.content

# print(c)

# Aplicando BeutifulSoup
soup = BeautifulSoup(c, "html.parser")
# print(soup.prettify())

# traigo todo las clases
all = soup.find_all("div", {"class": "cities"})
# print(all[0])

all2 = soup.find_all("h2")
# print(all2)

titulo = soup.find_all("h2")[0].text
# print(titulo)

# extraigo todos los titulos
titulos = all
for t in all:
    print(t.find_all("h2")[0].text)

# Extraigo todos los parrafos
parrafos = all
for p in parrafos:
    print(p.find_all("p")[0].text)
