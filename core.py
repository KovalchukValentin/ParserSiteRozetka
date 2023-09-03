import requests
from bs4 import BeautifulSoup


class Parcer:
    def __init__(self, url):
        self.response = self.get_work_response(url)
        self.links = self.get_all_links()
        self.max_page = self.get_max_page(links=self.links)

    def get_work_response(self, url) -> requests.Response:
        response = requests.get(url)
        if response.status_code == 200:
            return response
        else:
            print('Failed to retrieve the webpage. Status code:', response.status_code)
            exit()

    def get_all_links(self) -> list:
        html_content = self.response.text
        soup = BeautifulSoup(html_content, 'html.parser')
        return soup.find_all('a')

    def get_max_page(self, links: list) -> int:
        num_of_page = 1
        for link in links:
            if self.is_bed_link(link):
                continue
            if (len(link.get('href').split('/')) > 4
                    and link.get('href').split('/')[4].split('=')[0] == 'page'):
                num_of_page = link.text
        return int(num_of_page)

    def is_bed_link(self, link) -> bool:
        return not link.text or not link.get('href')

    def get_all_models_of_mobile(self) -> list:
        return self._get_all_a_with_class(class_="goods-tile__heading ng-star-inserted")

    # def _get_all_models_of_mobile(self, links) -> list:
    #     models_of_mobile = []
    #     flag_top = 2
    #     for link in links:
    #         if self.is_bed_link(link):
    #             continue
    #         if link.get('href')[0] == '/' or link.text[1].isnumeric():
    #             continue
    #         if flag_top:
    #             if flag_top == 1:
    #                 flag_top -= 1
    #             elif link.get('href') == 'https://rozetka.com.ua/ua/':
    #                 flag_top -= 1
    #             continue
    #         if link.get('href') == 'https://rozetka.com.ua/ua/contacts/':
    #             return models_of_mobile
    #         models_of_mobile.append(link)

    def _get_all_a_with_class(self, class_):
        html_content = self.response.text
        soup = BeautifulSoup(html_content, 'html.parser')
        return soup.find_all("a", class_=class_)

