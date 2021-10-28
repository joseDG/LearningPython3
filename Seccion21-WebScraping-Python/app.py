import requests
import bs4

# obtengo la informacion de la url de ejemplo
result = requests.get("http://www.example.com")

# Me permite saber cual es el tipo de archivo
# print(type(result))
print(result.text)

# esta libreria se la importa para obtener de mejor forma los elementos
soup = bs4.BeautifulSoup(result.text, "lxml")
print(soup)

# Aqui se obtiene el texto de los h1
print(soup.select('h1')[0].getText())

# aqui se obtiene los parrafos de la pagina web
site_paragraphs = soup.select("p")
print(site_paragraphs[0].getText())
