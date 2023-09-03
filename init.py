from core import Parcer
from analyst import Analyst


def view(links):
    for link in links:
        print(link.text)


def analysis(values):
    analyst.add_values(values)
    print(f'Sum={analyst.sum_values},'
          f'Averange={analyst.get_averange()}'
          f'Min={analyst.min_value},'
          f'Max={analyst.max_value}')


if __name__ == "__main__":
    url = 'https://rozetka.com.ua/ua/mobile-phones/c80003/'
    parser = Parcer(url=url)
    analyst = Analyst()
    [analysis(result) for result in parser.get_all_values_from_first_pages_in_int_list(10)]