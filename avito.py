import requests
from bs4 import BeautifulSoup

#https://www.avito.ru/novosibirsk/kvartiry?p=100

url = 'https://www.avito.ru/novosibirsk/kvartiry?p=1'

def get_html(url):
	r = requests.get(url)
	return r.text

def get_total_pages(html):
	soup = BeautifulSoup(get_html(url), 'lxml')
	pages = soup.find('div', class_='pagination-pages').find_all('a', class_='pagination-page')[-1].get('href')
	total_pages = pages.split('=')[1].split('&')[0]
	return int(total_pages)

def get_page_data(html):
	soup = BeautifulSoup(html, 'lxml')
	ads = soup.find('div', class_='catalog-list')


def main():
	base_url = 'https://www.avito.ru/novosibirsk/kvartiry?p='
	total_pages = get_total_pages(get_html(url))
	for i in range(1, 3):
		url_gen = base_url + str(i)
		html = get_html(url_gen)
		get_page_data(html)

if __name__ == '__main__':
	main()


	#js-catalog_before-ads
	#item_table