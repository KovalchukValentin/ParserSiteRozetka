from core import Parcer


def view(links):
    for link in links:
        print(link.text)


if __name__ == "__main__":
    url = 'https://rozetka.com.ua/ua/mobile-phones/c80003/'
    parser = Parcer(url=url)
    view(parser.get_all_models_of_mobile())
