import requests
from bs4 import BeautifulSoup


class Parcer:
    def __init__(self, url):
        self.url = url
        self.response = self._get_work_response(self.url)
        self.max_page = self.get_max_page()

    def _change_response(self, url):
        self.response = self._get_work_response(url)

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
        return int(self._get_all_tag_with_class(tag="a", class_="pagination__link ng-star-inserted")[-1].text)

    def get_all_link_tiles_from_first_pages(self, pages=10) -> list:
        for result in self._get_all_tag_with_class_from_first_pages(tag="a",
                                                                    class_="goods-tile__heading ng-star-inserted",
                                                                    pages=pages):
            yield result

    def get_all_values_from_first_pages_in_int_list(self, pages=10) -> list:
        for result in self._get_all_tag_with_class_from_first_pages(tag="span",
                                                                    class_="goods-tile__price-value",
                                                                    pages=pages):
            int_result = []
            for value in result:
                int_result.append(self.convert_value_from_site_to_int(value=value.text))
            yield int_result

    def convert_value_from_site_to_int(self, value: str) -> int:
        return int(value[:-1:].replace(' ', ''))

    def _get_all_tag_with_class_from_first_pages(self, tag, class_, pages) -> list:
        if pages >= self.max_page:
            pages = self.max_page
        current_page = 1
        while current_page <= pages:
            current_url = self.url + f"page={current_page}"
            self._change_response(current_url)
            yield self._get_all_tag_with_class(tag=tag, class_=class_)
            print(f"Done: {round(current_page / pages * 100)}%")
            current_page += 1

    def _get_all_tag_with_class(self, tag: str, class_: str) -> list:
        html_content = self.response.text
        soup = BeautifulSoup(html_content, 'html.parser')
        return soup.find_all(tag, class_=class_)
