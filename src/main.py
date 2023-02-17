import requests
from bs4 import BeautifulSoup

url_measures = "https://myrosmol.ru/measures"
url_test = "https://myrosmol.ru/measures/2"

def check_status_code(status_code: int) -> bool:
    """
    The function check your status code after requests
    :param status_code: Status of response
    :type status_code: :obj: `int`
    :return: True or False
    :type: :obj: `str`
    """
    return True if status_code == 200 else False


def get_measures(url: str) -> list[str]:
    """
    The function get all measures from FGASI
    :param url: Url path
    :return: Measures
    :type: :obj: `str`
    """
    response = requests.get(url)
    # print(response.status_code)
    if check_status_code(response.status_code):
        soup = BeautifulSoup(response.content, "html.parser")
        print(soup.prettify())

        temp = soup.find_all("div", {"class": "col-md-6 d-flex"})
        for i in temp:
            print(i)


def start_event_loop() -> None:
    """
    The function start all process
    :return: None
    :type: :obj: `None`
    """
    get_measures(url_test)


if __name__ == "__main__":
    start_event_loop()