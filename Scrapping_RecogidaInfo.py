import requests
from bs4 import BeautifulSoup

req = requests.get('https://en.wikipedia.org/wiki/Python_(programming_lenguage)')
soup = BeautifulSoup(req.text, "lxml")
print (soup.title)


for sub_heading in soup.find_all('h1'):
    print(sub_heading.text)
