import requests
from bs4 import BeautifulSoup
import csv

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


#Проблемы с кодировкой
def write_csv(data):
    with open('avito.csv', 'a', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow( (data['title'], data['price'], data['metro'], data['url']) )


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    ads = soup.find('div', class_='catalog-list').find_all('div', class_='item_table')
    for ad in ads:
        
        try:
            title = ad.find('div', class_='description').find('h3').text.strip()
        except:
            title = 'title'
        
        try:
            url = ad.find('div', class_='description').find('h3').find('a').get('href')
        except:
            url = 'url'
        
        try:
            price = ad.find('div', class_='about').text.strip()
        except:
            price = 'price'

        try:
            metro = ad.find('p', class_='address').text.strip()
        except:
            metro = 'metro'

        data = {'title': title, 
                'url': url, 
                'price': price, 
                'metro': metro}

        #print(data)

        write_csv(data)

def main():
    base_url = 'https://www.avito.ru/novosibirsk/kvartiry?p='
    total_pages = get_total_pages(get_html(url))
    for i in range(1, 2):
        url_gen = base_url + str(i)
        html = get_html(url_gen)
        get_page_data(html)

if __name__ == '__main__':
    main()
