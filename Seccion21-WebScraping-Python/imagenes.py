import requests
import bs4

res = requests.get("https://es.wikipedia.org/wiki/Deep_Blue_(computadora)")
soup = bs4.BeautifulSoup(res.text, 'lxml')

# Se obtiene la iamgen
# print(soup.select('img')[0])

computer = soup.select('img')[0]
print(computer['src'])

imagen_link = requests.get(
    'https: // upload.wikimedia.org/wikipedia/commons/thumb/b/be/Deep_Blue.jpg/300px-Deep_Blue.jpg')

f = open('My_computer.jpg', 'wb')
f.write(imagen_link.content)
f.close()
