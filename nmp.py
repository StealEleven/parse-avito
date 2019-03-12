import csv

import requests
from bs4 import BeautifulSoup
import codecs

#https://www.avito.ru/novosibirsk/kvartiry?p=100

url = 'https://nea2048.ru/nmp.html'

def get_html(url):
    r = requests.get(url)
    return r.text

def get_total_pages(html):
    soup = BeautifulSoup(get_html(url), 'lxml')
    pages = soup.find('div', class_='pagination-pages').find_all('a', class_='pagination-page')[-1].get('href')
    total_pages = pages.split('=')[1].split('&')[0]
    return int(total_pages)


#Проблемы с кодировкой
def write_csv(data):
	#codecs.open
    with open('nmp.csv', 'a', encoding='utf-8', errors='ignore') as f:
        writer = csv.writer(f)
        writer.writerow( (data['is_b4w'], data['img_link'], data['item_group'], data['item_name'], data['item_art']) )


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    ads = soup.find('ul', class_='nmp-product-list_cat-items').find_all('li')
    print(len(ads))
    for ad in ads:
        try:
        	is_b4w = ad.find('div', class_='nmp-item-cat_image-wrap').find('a', class_='nmp-item-cat_render-link').get('href')
        except:
        	print("no b4w")
        	continue
        try:
            img_link = ad.find('div', class_='nmp-item-cat_image-wrap').find('img').get('src')
        except:
            img_link = 'img_link'
        
        try:
            item_group = ad.find('div', class_='nmp-item-cat_data-wrap').find('a').find('span').text.strip()
        except:
            item_group = 'item_group'
        
        try:
            item_name = ad.find('div', class_='nmp-item-cat_data-wrap').find('h2').find('span', itemprop='name').text.strip()
        except:
            item_name = 'item_name'

        try:
            item_art = ad.find('div', class_='nmp-item-cat_data-wrap').find('p', class_='__secondary').text.strip()
        except:
            item_art = 'item_art'

        data = {'is_b4w': is_b4w,
        		'img_link': img_link, 
                'item_group': item_group, 
                'item_name': item_name, 
                'item_art': item_art}
        write_csv(data)

def main():
	html = get_html(url)
	get_page_data(html)

#    base_url = 'https://www.avito.ru/novosibirsk/kvartiry?p='
#    total_pages = get_total_pages(get_html(url))
#    for i in range(1, 2):
#        url_gen = base_url + str(i)
#        html = get_html(url_gen)
#        get_page_data(html)

if __name__ == '__main__':
    main()
