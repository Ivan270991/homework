import requests
from bs4 import BeautifulSoup

url="https://habr.com/ru/top/monthly/"
r = requests.get(url)
soup = BeautifulSoup(soup.content,'html.parser')
h1=soup.find_all('h2', {'class':"post__title"}).text
print(list(h1))