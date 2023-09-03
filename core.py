import requests
from bs4 import BeautifulSoup


class Parcer:
    def __init__(self, url):
        self.response = self._get_work_response(url)
        self.links = self.get_all_links()
        self.max_page = self.get_max_page()

    def _get_work_response(self, url) -> requests.Response:
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

    def get_max_page(self) -> int:
        return int(self._get_all_a_with_class(class_="pagination__link ng-star-inserted")[-1].text)

    def get_all_models_of_mobile(self) -> list:
        return self._get_all_a_with_class(class_="goods-tile__heading ng-star-inserted")

    def _get_all_a_with_class(self, class_):
        html_content = self.response.text
        soup = BeautifulSoup(html_content, 'html.parser')
        return soup.find_all("a", class_=class_)

