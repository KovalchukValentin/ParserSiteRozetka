from core import Parcer


def view(links):
    for link in links:
        print(link)


if __name__ == "__main__":
    url = 'https://rozetka.com.ua/ua/mobile-phones/c80003/'
    parser = Parcer(url=url)
    [view(result) for result in parser.get_all_values_from_first_pages_in_int_list(2)]