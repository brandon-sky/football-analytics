from bs4 import BeautifulSoup
from requests import Session

from connectivity.toWebsite import request_url, parse_html_to_soup


from typing import Tuple

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
URL ="https://www.pro-football-reference.com"
BASE_URL = URL+"/boxscores"


def extract_current_week_info(soup: BeautifulSoup) -> str:
    h2_element = soup.select_one('h2').text
    return h2_element

def extract_all_boxscore_links(soup: BeautifulSoup) -> list:
    final_links = soup.select('a:-soup-contains("Final")')
    return [BASE_URL+link["href"] for link in final_links]

def main():
    # Request from site
    http_session = Session()
    html = request_url(session=http_session, url=BASE_URL)
    soup = parse_html_to_soup(html=html)

    # Extract
    last_gameday = extract_current_week_info(soup=soup)
    boxscore_links = extract_all_boxscore_links(soup=soup)

    # Load
    links_to_crawl = {
        last_gameday: boxscore_links
    }

    print(links_to_crawl)
    return

if __name__ == "__main__":
    main()