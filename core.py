

import requests
from bs4 import BeautifulSoup


def get_max_page(links: list) -> int:
    num_of_page = 1
    for link in links:
        if is_bed_link(link):
            continue
        if (len(link.get('href').split('/')) > 4
                and link.get('href').split('/')[4].split('=')[0] == 'page'):
            num_of_page = link.text
    return int(num_of_page)


def is_bed_link(link):
    return not link.text or not link.get('href')



url = 'https://rozetka.com.ua/ua/mobile-phones/c80003/'
response = requests.get(url)

if response.status_code == 200:
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')
    links = soup.find_all('a')
    pages = soup.find_all('page=')
    max_page = get_max_page(links=links)

    for link in links:

        '''print('Text:', link.text)
        print('URL:', link.get('href').split('/'))'''
        '''if (link.text.split()[0] == "Мобільний"):
            print('Text:', link.text)
            print('URL:', link.get('href'))'''

else:
    print('Failed to retrieve the webpage. Status code:', response.status_code)
    exit()




