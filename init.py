from core import Parcer


def view(links):
    for link in links:
        print(link.text)


if __name__ == "__main__":
    url = 'https://rozetka.com.ua/ua/mobile-phones/c80003/'
    parser = Parcer(url=url)
    [view(result) for result in parser.get_all_link_tiles_from_first_pages(2)]