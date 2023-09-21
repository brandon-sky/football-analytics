from bs4 import BeautifulSoup
from requests import Session

from connectivity.toWebsite import request_url, parse_html_to_soup


from typing import Tuple

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
URL ="https://www.pro-football-reference.com"
BASE_URL = URL+"/boxscores"




def extract_current_week_info(soup: BeautifulSoup) -> Tuple[str]:
    h2_element = soup.select_one('h2').text
    return h2_element.split()


def main():
    http_session = Session()
    html = request_url(session=http_session, url=BASE_URL)
    soup = parse_html_to_soup(html=html)
    last_gameday = extract_current_week_info(soup=soup)
    print(f"{last_gameday = }")
    return

if __name__ == "__main__":
    main()