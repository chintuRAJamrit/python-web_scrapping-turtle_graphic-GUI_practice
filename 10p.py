import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Sachin_Tendulkar'
response = requests.get(url)

soup = BeautifulSoup(response.content , 'html.parser')

img_link = [img['src'] for img in soup.find_all('img')]

for link in img_link:
    print(link)
