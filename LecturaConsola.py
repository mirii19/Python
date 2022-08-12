import requests
from bs4 import BeautifulSoup

url = input("Escribe la direccion: ")

req = requests.get("http://"+url)
data = req.text
soup = BeautifulSoup(data, "lxml")
print (soup.title)


for sub_heading in soup.find_all('img'):
    print(sub_heading.get('src'))
