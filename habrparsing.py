import requests
from bs4 import BeautifulSoup

def get_html(url):
	r = requests.get(url)
	return r.text

def get_data(html):
	soup = BeautifulSoup(html,'lxml')
	h1=list(soup.find_all('h2', {'class':"post__title"}))
	x=[i.text for i in h1]
	return x


def main():
	url="https://habr.com/ru/top/monthly/"
	print(get_data(get_html(url)))




if __name__=='__main__':
	main()