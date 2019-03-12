import requests
from bs4 import BeautifulSoup


#https://www.avito.ru/novosibirsk/kvartiry?p=100

url = 'https://www.avito.ru/novosibirsk/kvartiry/studiya_34_m_1010_et._1302410379'


def get_html(url):
    r = requests.get(url)
    return r.text

def get_items(html):
	soup = BeautifulSoup(html, 'lxml')
	test = soup.find_all('script')[0].string()

def main():
	html = get_html(url)
	items = get_items(html)
	print(items)

if __name__ == '__main__':
	main()

# https://www.avito.ru/items/phone/1302410379?pkey=59d293d9c68d5f7783e2272abc29079c&vsrc=r
# https://www.avito.ru/items/phone/1302410379?pkey=56460b6d141c99c0251c0781105bbe19&vsrc=r
# https://www.avito.ru/items/phone/1302410379?pkey=37b5179746dea3da78fe650c1b08938d&vsrc=r
# https://www.avito.ru/items/phone/1302410379?pkey=4909a565be43e872bdc7401f50d1e189&vsrc=r