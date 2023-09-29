import requests
from bs4 import BeautifulSoup


class Parcer:
    def __init__(self, url):
        self.url = url
        self.response = self._get_work_response(self.url)
        # self.max_page = self.get_max_page()

    def _change_response(self, url):
        self.response = self._get_work_response(url)

    def _get_work_response(self, url) -> requests.Response:
        response = requests.get(url)
        if response.status_code == 200:
            return response
        else:
            raise ValueError(f"Response error code {response.status_code}")

    def get_all_links(self) -> list:
        html_content = self.response.text
        soup = BeautifulSoup(html_content, 'html.parser')
        return soup.find_all('a')

    def get_all_tag_with_class(self, tag: str, class_: str) -> list:
        html_content = self.response.text
        soup = BeautifulSoup(html_content, 'html.parser')
        return soup.find_all(tag, class_=class_)
